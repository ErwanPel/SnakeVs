<h2 align="center">

</h2>

<h1 align="center">
SnakeVS

</h1>

</br>

<p align="center">
	<img alt="Last Commit" src="https://img.shields.io/github/last-commit/ErwanPel/SnakeVs_PythonGame.svg?style=flat-square">
	<img alt="Licence" src="https://img.shields.io/github/license/ErwanPel/SnakeVs_PythonGame.svg?style=flat-square">
	<img alt="Star" src="https://img.shields.io/badge/you%20like%20%3F-STAR%20ME-blue.svg?style=flat-square">
</p>



## Tech Stack



**Server:** Python


## Overview

This project is my first game in Python. The player controls the green snake and the computer is the red snake. To score a point, the player must eat all 10 blue marbles without being touched by the red snake, without eating itself and without leaving the game. Otherwise, the player returns to 0 points. The red snake can also gain points, grow and will try to attack you if you're close to its head.

For the control :

1) top arrow: go up,
2) right arrow: go right,
3) down arrow: go down,
4) left arrow: go left,

You can change the window size at the value level: "NB_COL" and "NB_ROW" and the size of each cell in "CELL_SIZE". 

For this line: pygame.time.set_timer(SCREEN_UPDATE, 150) => You can change the speed of the game by playing on the number. The lower the number, the faster the snakes will be. 

You can change the victory conditions in the "def victory(self)" part and the defeat conditions in the part: "def game_over(self)"

### Running the project

Clone this repository :

```
git clone https://github.com/ErwanPel/SnakeVs_PythonGame.git
cd SnakeVs_PythonGame
```

**Install packages with Visual Studio Code :**

1) You must create the python environment in visual studio code. For this, in the command palette, look for "Python: Create an environment ...", select venv or conda and choose your interpreter.
2) You need to install a Python terminal. For this, in the command palette, look for "Python: create a terminal...".
3) You must install the Pygame module:

```
pip install pygame

```

When installation is complete, you have to launch  :

```
py main.py

```

**Install packages with PyCharm :**

1) Python interpreter setup: File > Settings > search tab named like this "Project: Name_of_Project" > Python Interpreter > select your interpreter.
2) Configure the execution file: under the navigation bar, click edit configuration to the left of the "running" button. In Configuration > Script path selectionne "SnakeVs_PythonGame main.py". Below, select the Python interpreter in the "Python Interpreter" field.
3) Install the pygame package: In View > Windows Tool > Terminal. Once the terminal is open:

```
pip install pygame

```

When installation is complete, you have to launch  :

```
py main.py

```

## Star, Fork, Clone & Contribute

Feel free to contribute on this repository. If my work helps you, please give me back with a star. This means a lot to me and keeps me going!
