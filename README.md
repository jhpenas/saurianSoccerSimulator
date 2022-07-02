<p align="center">
  <img src="/static/sss.png" >
</p>

# Saurian Soccer Simulator
<sub>Em Português [aqui](https://github.com/jhpenas/saurianSoccerSimulator/blob/main/README%20pt.md).</sub>

<sub>Developed as the Final Project for Harvard [CS50's Introduction to Computer Science](https://learning.edx.org/course/course-v1:HarvardX+CS50+X/home).</sub>

<sub>[More Projects](https://github.com/jhpenas/portfolio).</sub>

The final application was deployed on heroku and it is available [here](http://saurian-soccer-simulator.herokuapp.com/) and the demonstration video [here](https://www.youtube.com/watch?v=7lDYlgxDh6Y)


## Main Page
This project consists in a website, made in Flask, and use some different languages, such as HTML5, CSS and JavaScript, SQL, and Python, of course. The website has soccer as theme as well as dinosaurs, which brings us to its name. The logo was also made by me, using Adobe Illustrator and free vectors disbonible at Freepik. The simulation of matches is the core of the web application, However it isn't all, Saurian Soccer Simulator has also Statitisc and Comparation tabs.
<p align="center">
  <img src="/Screenshots/index.png" >
</p>

## Simulate
In the simulation tab, Saurian Soccer Simulator can predict the result for a soccer match and the simulation is made using the open-source CatBoost regressor, a machine learning algorithm that uses gradient boosting on decision tree, only considering previous home and away results for the home and away teams, respectively, on the database. Another consideration is that the simulation is made as if the game took place immediately after the last one in the database.

<p align="center">
  <img src="/Screenshots/Simulation 2.png" >
</p>
<p align="center">
  <img src="/Screenshots/Simulation 3.png" >
</p>



## Statistics
The website also has statistics tabs: statistics properly and comparation. In the statistics tab, you can choose a team and view its wins, losses and draws on all matches in  the database presented dynamic graphics, made with JavaScript, such as pie charts and a line chart showing team's performance throught seasons. 
<p align="center">
  <img src="/Screenshots/Statistics 1.png" >
</p>
<p align="center">
  <img src="/Screenshots/Statistics 2.png" >
</p>
<p align="center">
  <img src="/Screenshots/Statistics 3.png" >
</p>



## Compare
In the comparation tab, you can make comparations between teams from the same country to see which one is the best, based on their previous results against each other, as shown below.
<p align="center">
  <img src="/Screenshots/Compare 1.png" >
</p>
<p align="center">
  <img src="/Screenshots/Compare 2.png" >
</p>
<p align="center">
  <img src="/Screenshots/Compare 3.png" >
</p>


The database used for this application belongs to Hugo Mathien and it is available [here](https://www.kaggle.com/hugomathien/soccer).

