<p align="center">
  <img src="/static/sss.png" >
</p>

# Saurian Soccer Simulator
<sub>In English [here]([https://github.com/jhpenas/portfolio](https://github.com/jhpenas/saurianSoccerSimulator/blob/main/README.md)).</sub>

<sub>Desenvolvido como projeto final do curso de Harvard [CS50's Introduction to Computer Science](https://learning.edx.org/course/course-v1:HarvardX+CS50+X/home).</sub>

<sub>[Mais Projetos](https://github.com/jhpenas/portfolio).</sub>

O aplicativo final está hospedado no heroku e está disponível [aqui](http://saurian-soccer-simulator.herokuapp.com/) e o vídeo de apresentação [aqui](https://www.youtube.com/watch?v=7lDYlgxDh6Y)


## Página Principal
Este projeto consiste em uma aplicação web, feita em Flask, utilizando algumas linguagens diferentes, como HTML5, CSS e JavaScript, SQL e Python. O site tem como tema o futebol e também os dinossauros, o que nos remete ao seu nome. O logotipo também foi feito por mim, usando Adobe Illustrator e vetores de livres utilização, disponíveis na Freepik. A simulação de partidas é o charme da aplicação, mas não é tudo: Saurian Soccer Simulator também possui abas de Estatísticas e Comparação entre times.

<p align="center">
  <img src="/Screenshots/index.png" >
</p>

## Simular
Na guia de simulação, o Saurian Soccer Simulator pode prever o resultado de uma partida de futebol, e a simulação é feita utilizando o regressor CatBoost, de código aberto, um algoritmo de aprendizado de máquina que usa gradient boosting na árvore de decisão, considerando apenas os resultados anteriores em casa e fora para o times. Outra consideração é que a simulação é feita como se o jogo ocorresse imediatamente após o último no banco de dados.

<p align="center">
  <img src="/Screenshots/Simulation 2.png" >
</p>
<p align="center">
  <img src="/Screenshots/Simulation 3.png" >
</p>

## Statistics
O site também possui abas de estatísticas: estatísticas propriamente ditas e comparação. Na aba de estatísticas, você pode escolher um time e visualizar suas vitórias, derrotas e empates em todas as partidas na base de dados apresentada em gráficos dinâmicos, feitos com JavaScript, como gráficos de pizza e um gráfico de linhas mostrando o desempenho do time ao longo das temporadas.

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
Na guia de comparação, você pode fazer comparações entre equipes do mesmo país para ver qual é a melhor, com base nos resultados anteriores entre si, conforme mostrado abaixo.
<p align="center">
  <img src="/Screenshots/Compare 1.png" >
</p>
<p align="center">
  <img src="/Screenshots/Compare 2.png" >
</p>
<p align="center">
  <img src="/Screenshots/Compare 3.png" >
</p>

A base de dados utilizada nesta aplicação pertence à Hugo Mathien e está disponível [aqui](https://www.kaggle.com/hugomathien/soccer).

