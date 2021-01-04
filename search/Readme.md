
## Acknowledgements 
The Pacman AI projects were developed at UC Berkeley. The
core projects and autograders were primarily created by John DeNero and Dan Klein.
Student side autograding was added by Brad Miller, Nick Hay, and Pieter Abbeel. We
thank them for their permission to use it as a part of this course.
## Introduction
In this project, your Pacman agent will find paths through his maze world, both to
reach a particular location and to collect food efficiently. You will build general search
algorithms and apply them to Pacman scenarios.
As in Project 0, this project includes an autograder for you to grade your answers on
your machine. This can be run with the command:  
**python3 autograder.py**  
## Question 1 (3 points): Finding a Fixed Food Dot using Depth First Search
Code successfully implements the following commands  
**python3 pacman.py -l tinyMaze -p SearchAgent  
python3 pacman.py -l mediumMaze -p SearchAgent  
python3 pacman.py -l bigMaze -z .5 -p SearchAgent**  
## Question 2 (3 points): Breadth First Search  
Code successfully implements the following commands  
**python3 pacman.py -l mediumMaze -p SearchAgent -a fn=bfs  
python3 pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5**  
## Question 3 (3 points): Varying the Cost Function  
Code successfully implements the following commands  
**python3 pacman.py -l mediumMaze -p SearchAgent -a fn=ucs  
python3 pacman.py -l mediumDottedMaze -p StayEastSearchAgent  
python3 pacman.py -l mediumScaryMaze -p StayWestSearchAgent**  
## Question 4 (3 points): A* search  
Code successfully implements the following command  
**python3 pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic**  
## Question 5 (3 points): Finding All the Corners  
Code successfully implements the following commands  
**python3 pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem  
python3 pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem**    
## Question 6 (3 points): Corners Problem: Heuristic  
Code successfully implements the following commands  
**python3 pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
Note: AStarCornersAgent is a shortcut for
-p SearchAgent -a fn=aStarSearch,prob=CornersProblem,heuristic=cornersHeuristic**  
Grading: Your heuristic must be a non-trivial non-negative consistent heuristic to
receive any points. Make sure that your heuristic returns 0 at every goal state and
never returns a negative value. Depending on how few nodes your heuristic expands,
you'll be graded:  
Number of nodes expanded Grade  
more than 2000 0/3  
at most 2000 1/3  
at most 1600 2/3  
at most 1200 3/3  
(This agents score below)  
![image](https://user-images.githubusercontent.com/47394267/103571922-bfd06300-4e99-11eb-9247-8a13a261e9ae.png)

## Question 7 (4 points): Eating All The Dots  
Code successfully implements the following command  
**python3 pacman.py -l trickySearch -p AStarFoodSearchAgent**  
Any non-trivial non-negative consistent heuristic will receive 1 point. Make sure that
your heuristic returns 0 at every goal state and never returns a negative value.
Depending on how few nodes your heuristic expands, you'll get additional points:  
Number of nodes expanded Grade  
more than 15000 1/4  
at most 15000 2/4  
at most 12000 3/4  
at most 9000 4/4 (full credit; medium)  
at most 7000 5/4 (optional extra credit; hard)  
While this implementation is very slow (52.3 seconds) it expands only 4137 nodes, giving us the extra credit point.  
![image](https://user-images.githubusercontent.com/47394267/103572298-54d35c00-4e9a-11eb-826b-b913caec4054.png)
## Question 8 (3 points): Suboptimal Search  
Code successfully implements the following command  
**python3 pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5**  

