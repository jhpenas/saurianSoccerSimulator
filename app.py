from flask import Flask, render_template, request, redirect
from cs50 import SQL
import pandas as pd
from assistfunctions import pizza, home_away, by_season


app = Flask(__name__)
# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///db_soccer.db")





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/simulate',methods=['GET', "POST"])
def simulate():
    if request.method == "GET":
        leagues = db.execute("SELECT name FROM League ORDER BY name ASC ")
        return render_template('simulate.html', leagues=leagues)
    else:
        league = request.form['league']
        try:
            league_id = db.execute("SELECT id FROM League WHERE name = :league",league=league)[0]['id']
        except:
            return render_template('error.html', error='noleague')
        teams = db.execute("SELECT DISTINCT team_long_name FROM (Match INNER JOIN Team ON Match.home_team_api_id = Team.team_api_id )WHERE Match.league_id = :league_id",league_id=league_id)

        return render_template('simulated.html',teams=teams)

@app.route('/simulated',methods=['GET', "POST"])
def simulated():

    if request.method == 'POST':
        team1 = request.form['team1']
        team2 = request.form['team2']
        from machinel import simulate_result


        try:
            team1_id = db.execute("SELECT team_api_id FROM Team WHERE team_long_name = :team",team=team1)[0]['team_api_id']
        except:
            return render_template('error.html', error='noteam')
        try:
            team2_id = db.execute("SELECT team_api_id FROM Team WHERE team_long_name = :team", team=team2)[0]['team_api_id']
        except:
            return render_template('error.html', error='noteam')

        matches = db.execute("SELECT season, home_team_api_id, away_team_api_id, home_team_goal, away_team_goal FROM Match WHERE home_team_api_id = :hteam OR away_team_api_id = :ateam", hteam=team1_id, ateam=team2_id)
        if team1_id == team2_id:
            return render_template('error.html', error='sameteam')
        elif len(matches) < 1:
            return render_template('error.html', error='nomatch')
        df_matches = pd.DataFrame(matches)
        result = simulate_result(home_team_id=team1_id,
                                 away_team_id=team2_id,
                                 df=df_matches)


        return render_template('simulated1.html',team1=team1, team2=team2, matches=df_matches, result=result)
    else:
        return redirect('/')

@app.route('/compare', methods=["GET", "POST"])
def compare():
    if request.method == "GET":
        teams = db.execute("SELECT team_long_name FROM Team ORDER BY team_long_name ASC ")
        return render_template('compare.html',teams=teams)
    else:
        team1 = request.form['team1']
        team2 = request.form['team2']
        try:
            team1_id = db.execute("SELECT team_api_id FROM Team WHERE team_long_name = :team1",team1=team1)[0]['team_api_id']
            team2_id = db.execute("SELECT team_api_id FROM Team WHERE team_long_name = :team2", team2=team2)[0][
                'team_api_id']
        except:
            return render_template('error.html', error='noteam')

        if team1_id == team2_id:
            return render_template('error.html', error='sameteam')
        years = db.execute("SELECT season FROM Match WHERE (home_team_api_id = :team1 AND away_team_api_id = :team2) OR (home_team_api_id = :team2 AND away_team_api_id = :team1)", team1=team1_id, team2=team2_id)
        matches = db.execute("SELECT match_api_id FROM Match WHERE (home_team_api_id = :team1 AND away_team_api_id = :team2) OR (home_team_api_id = :team2 AND away_team_api_id = :team1)", team1=team1_id, team2=team2_id)
        nmatches = len(matches)
        if nmatches > 0:
            competitions = db.execute(
                "SELECT DISTINCT (league_id) FROM Match WHERE (home_team_api_id = :team1 AND away_team_api_id = :team2) OR (home_team_api_id = :team2 AND away_team_api_id = :team1)",
                team1=team1_id, team2=team2_id)[0]['league_id']
            leagues = db.execute("SELECT name FROM League WHERE id=:c", c=competitions)[0]['name']
            draws = db.execute(
                "SELECT  COUNT (id) FROM Match WHERE ((home_team_api_id = :team1 AND away_team_api_id = :team2) OR (home_team_api_id = :team2 AND away_team_api_id = :team1)) AND home_team_goal = away_team_goal",
                team1=team1_id, team2=team2_id)[0]['COUNT (id)']
            team1_goals = 0
            team1_goals += db.execute(
                "SELECT SUM (home_team_goal) FROM Match WHERE home_team_api_id =:id1 AND away_team_api_id = :id2",
                id1=team1_id, id2=team2_id)[0]['SUM (home_team_goal)']

            team1_goals += db.execute(
                "SELECT SUM (away_team_goal) FROM Match WHERE home_team_api_id =:id2 AND away_team_api_id = :id1",
                id1=team1_id, id2=team2_id)[0]['SUM (away_team_goal)']

            team2_goals = 0
            team2_goals += db.execute(
                "SELECT SUM (home_team_goal) FROM Match WHERE home_team_api_id =:id2 AND away_team_api_id = :id1",
                id1=team1_id, id2=team2_id)[0]['SUM (home_team_goal)']

            team2_goals += db.execute(
                "SELECT SUM (away_team_goal) FROM Match WHERE home_team_api_id =:id1 AND away_team_api_id = :id2",
                id1=team1_id, id2=team2_id)[0]['SUM (away_team_goal)']

            team1_wins = 0
            team1_wins += db.execute(
                "SELECT COUNT (id) FROM Match WHERE home_team_api_id =:id1 AND away_team_api_id = :id2 AND home_team_goal > away_team_goal",
                id1=team1_id, id2=team2_id)[0]['COUNT (id)']

            team1_wins += db.execute(
                "SELECT COUNT (id) FROM Match WHERE home_team_api_id =:id2 AND away_team_api_id = :id1 AND home_team_goal < away_team_goal",
                id1=team1_id, id2=team2_id)[0]['COUNT (id)']

            team2_wins = 0
            team2_wins += db.execute(
                "SELECT COUNT (id) FROM Match WHERE home_team_api_id =:id1 AND away_team_api_id = :id2 AND home_team_goal < away_team_goal",
                id1=team1_id, id2=team2_id)[0]['COUNT (id)']

            team2_wins += db.execute(
                "SELECT COUNT (id) FROM Match WHERE home_team_api_id =:id2 AND away_team_api_id = :id1 AND home_team_goal > away_team_goal",
                id1=team1_id, id2=team2_id)[0]['COUNT (id)']

            graph = pizza([team1_wins,team2_wins,draws],
                          labels=[team1+' Wins', team2+' Wins', 'Draws'],
                          colors = ["#DAA520", "#D2691E", "#FDB45C"])

            goals_graph = zip([team1_goals, team2_goals], [team1+' Goals', team2+' Goals'], ["#DAA520", "#D2691E"])


            return render_template('compared.html',
                                   team1=team1,
                                   team2=team2,
                                   nmatches= nmatches,
                                   years=years,
                                   comp=leagues,
                                   draws = draws,
                                   team1_goals = team1_goals,
                                   team2_goals = team2_goals,
                                   team1_wins = team1_wins,
                                   team2_wins = team2_wins,
                                   graph=graph,
                                   goals_graph=goals_graph,
                                   have_matches=True)
        else:
            return render_template('compared.html',
                                   team1=team1,
                                   team2=team2,
                                   have_matches = False)


@app.route('/statistics', methods=["GET", "POST"])
def stats():
    if request.method == "GET":
        teams = db.execute("SELECT team_long_name FROM Team ORDER BY team_long_name ASC ")
        return render_template('stats.html',teams=teams)
    else:
        team = request.form['team']

        try:
            team_id = db.execute("SELECT team_api_id FROM Team WHERE team_long_name =:name", name=team)[0]['team_api_id']
        except:
            return render_template('error.html', error='noteam')
        home_pie, away_pie = home_away(db=db,team_id=team_id)
        performance_home, performance_away, performance_total, season = by_season(db, team_id)
        league_id = db.execute("SELECT DISTINCT league_id FROM Match WHERE home_team_api_id=:teamid",teamid=team_id)[0]['league_id']
        league = db.execute("SELECT name FROM League WHERE id=:league_id",league_id=league_id)[0]['name']

        return render_template('statistics.html',
                               team=team,
                               season=season,
                               set1=home_pie,
                               set2=away_pie,
                               home_season_values = performance_home[1],
                               home_season_labels = performance_home[0],
                               away_season_values = performance_away[1],
                               away_season_labels = performance_away[0],
                               total_season_values = performance_total[1],
                               total_season_labels = performance_total[0],
                               league=league)

if __name__ == '__main__':
    app.run(debug=True)