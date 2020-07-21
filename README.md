# A* Maze Router

This program is a program that reads a file of netlists, and connect each net together using the A* algorithm.

## How to run on MacOS

* You need python 3 to be installed on your machine
* Save the downloaded folder on the desktop
* Open terminal and run the following command (change "USERNAME" to your logged in profile username:
```bash
cd /Users/"USERNAME"/Desktop/AStarRouter
python3 ./Simulation.py
```
* Then, enter the address of the input file.
* There is an input file called: input.txt is attached, and contains 8 test-cases.
* The output will be in a file with the name of the input and out is added to the name.
_Ex: if input is file.txt, output will be stored in the same directory in a file called: file_out.txt_

## Assumptions
* Default grid layout is: 1000x1000
* The number of times the code is going to switch between layers (if needed) is set to 1 (Cost)

## Limitations
* Works perfectly for 2 layers, but some glitches appear beyond 2 layers

## Contributors
* Ramy ElGendi
* Ali Moussa

Under supervision of Dr. Mohamed Shalan in the Digital Design 2 Course, at the American University in Cairo.
