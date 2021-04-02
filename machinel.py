import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import confusion_matrix, r2_score
from catboost import CatBoostRegressor

def simulate_result(home_team_id, away_team_id, df):
    df = df

    df.season = df.season.str[-4:]
    df.season = pd.to_datetime(df.season, format='%Y').dt.year
    df_predict = pd.DataFrame([df.season,
                           df.home_team_api_id,
                           df.away_team_api_id,
                           df.home_team_goal,
                           df.away_team_goal])
    df_predict = df_predict.transpose()

    X = df_predict.iloc[:,:-2].values
    hgoals = df_predict.iloc[:, -2].values
    agoals =  df_predict.iloc[:, -1].values

    XH_train, XH_test, YH_train, YH_test = train_test_split(X, hgoals, test_size=0.2)
    XA_train, XA_test, YA_train, YA_test = train_test_split(X, agoals, test_size=0.2)




    regressorH = CatBoostRegressor()
    regressorH.fit(XH_train, YH_train)
    YH_pred = regressorH.predict(XH_test)
    acH = r2_score(YH_test,YH_pred)

    regressorA = CatBoostRegressor()
    regressorA.fit(XA_train, YA_train)
    YA_pred = regressorA.predict(XA_test)
    acA = r2_score(YA_test,YA_pred)




    season = max(df.season)

    h_goal = int(regressorH.predict([season, home_team_id, away_team_id]))
    a_goal = int(regressorA.predict([season, home_team_id, away_team_id]))
    return (h_goal, a_goal)
