from cs50 import SQL


def pizza(wld,labels=['Wins','Losses','Draws'],colors = ["#46BFBD", "#F7464A", "#FDB45C"]):
    values = wld
    return zip(values, labels, colors)

def home_away(db, team_id):
    home_wins = \
        db.execute("SELECT COUNT(id) FROM Match WHERE home_team_api_id =:id AND home_team_goal > away_team_goal",
                   id=team_id)[0]['COUNT(id)']

    home_loss = \
        db.execute("SELECT COUNT(id) FROM Match WHERE home_team_api_id =:id AND home_team_goal < away_team_goal",
                   id=team_id)[0]['COUNT(id)']

    home_draws = \
        db.execute("SELECT COUNT(id) FROM Match WHERE home_team_api_id =:id AND home_team_goal = away_team_goal",
                   id=team_id)[0]['COUNT(id)']

    home_pie = pizza([home_wins, home_loss, home_draws])

    away_wins = \
        db.execute("SELECT COUNT(id) FROM Match WHERE away_team_api_id =:id AND home_team_goal < away_team_goal",
                   id=team_id)[0]['COUNT(id)']

    away_loss = \
        db.execute("SELECT COUNT(id) FROM Match WHERE away_team_api_id =:id AND home_team_goal > away_team_goal",
                   id=team_id)[0]['COUNT(id)']

    away_draws = \
        db.execute("SELECT COUNT(id) FROM Match WHERE away_team_api_id =:id AND home_team_goal = away_team_goal",
                   id=team_id)[0]['COUNT(id)']

    away_pie = pizza([away_wins, away_loss, away_draws])
    return home_pie, away_pie



def graph_performance_season(performance):
    labels = []
    values = []
    for season in performance.keys():
        labels.append(season)
        values.append(performance[season])
    return [labels,values]




def by_season(db, team_id):
    seasons = db.execute("SELECT DISTINCT season FROM Match WHERE home_team_api_id =:team_id", team_id=team_id)
    s = []
    for season in seasons:
        s.append(season['season'])
    home_wins = {}
    home_matches = {}
    home_draw = {}
    away_wins = {}
    away_matches = {}
    away_draw = {}
    performance_home = {}
    performance_away = {}
    performance_total = {}
    for season in s:
        home_wins[season] = db.execute("SELECT COUNT(id) FROM Match WHERE home_team_api_id =:team_id AND home_team_goal > away_team_goal AND season =:season",
            team_id=team_id,season=season)[0]['COUNT(id)']

        home_draw[season] = db.execute("SELECT COUNT(id) FROM Match WHERE home_team_api_id =:team_id AND home_team_goal = away_team_goal AND season =:season",
            team_id=team_id,season=season)[0]['COUNT(id)']


        home_matches[season] = db.execute("SELECT COUNT(id) FROM Match WHERE home_team_api_id =:team_id AND season =:season", team_id=team_id,season=season)[0]['COUNT(id)']

        away_wins[season] = db.execute(
            "SELECT COUNT(id) FROM Match WHERE away_team_api_id =:team_id AND home_team_goal < away_team_goal AND season =:season",
            team_id=team_id,season=season)[0]['COUNT(id)']

        away_draw[season] = db.execute(
            "SELECT COUNT(id) FROM Match WHERE away_team_api_id =:team_id AND home_team_goal = away_team_goal AND season =:season",
            team_id=team_id,season=season)[0]['COUNT(id)']

        away_matches[season] = db.execute("SELECT COUNT(id) FROM Match WHERE away_team_api_id =:team_id AND season =:season",
                                          team_id=team_id,season=season)[0]['COUNT(id)']


        performance_home[season] = round(((home_wins[season] * 3 + home_draw[season])/ (home_matches[season] * 3)) * 100, 1)
        performance_away[season] = round(((away_wins[season] * 3 + away_draw[season]) / (away_matches[season] * 3)) * 100, 1)
        performance_total[season] = round(((home_wins[season] * 3 + home_draw[season] + away_wins[season] * 3 + away_draw[season])/(home_matches[season] * 3 + away_matches[season] * 3)) * 100, 1)
        p_home = graph_performance_season(performance_home)
        p_away = graph_performance_season(performance_away)
        p_total = graph_performance_season(performance_total)

        boarders = [s[0], s[len(s)-1]]
    return p_home, p_away, p_total, boarders