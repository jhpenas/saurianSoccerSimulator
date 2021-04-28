<p align="center">
  <img src="/static/sss.png" >
</p>

# Saurian Soccer Simulator
<sub>Developed as the Final Project for [CS50's Introduction to Computer Science](https://learning.edx.org/course/course-v1:HarvardX+CS50+X/home).</sub>

<sub>[More Projects](https://github.com/jhpenas/portfolio).</sub>

The final application is disponible [here](http://saurian-soccer-simulator.herokuapp.com/) and the demonstration video [here](https://www.youtube.com/watch?v=7lDYlgxDh6Y)

This project consists in a website, made in Flask, HTML5, CSS and JavaScript, which has soccer simulation as its core, and has also statistics and comparations functions.

The simulation is made using the open-source CatBoost regressor, a machine learning algorithm that uses gradient boosting on decision tree, only considering previous home and away results for the home and away teams, respectively. Another consideration is that the simulation is made as if the game took place immediately after the last one in the database.

The website also has statistics tabs: statistics properly and comparation. In the statistics tab, you can choose a team and view its wins, losses and draws on all matches in  the database presented dynamic graphics, made with JavaScript, such as pie charts and a line chart showing team's performance throught seasons. 

In the comparation tab, you can make comparations between teams from the same country to see which one is the best.

The database used for this application belongs to Hugo Mathien and it is disponible [here](https://www.kaggle.com/hugomathien/soccer).

