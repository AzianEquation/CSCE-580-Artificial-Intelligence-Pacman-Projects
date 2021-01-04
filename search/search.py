# Student: John Esco (2020)
# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    "*** YOUR CODE HERE ***"
    '''
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    '''
    # prints: [('B', '0:A->B', 1.0), ('C', '1:A->C'), ('D', '2:A->D', 4.0)]
    # import the directions that are valid
    # get Pacman's start position
    start = problem.getStartState()
    # verify that start is not the goal state, if so return empty moves array
    if problem.isGoalState(start):
        return []
    # initialize stack that will be used for the fringe
    fringeStack = util.Stack()
    # initialize the set that holds the visited nodes (set since no repeats)
    setOfVisited = set()
    # push list of (currNode, pathToCurr) to stack
    fringeStack.push((start, []))
    # while loop that iterates until stack is empty
    while not fringeStack.isEmpty():
        # pop from fringeStack (currNode, pathToCurr)
        nodePop = fringeStack.pop()
        # break up list into individual elements
        currNode = nodePop[0]
        pathStart = nodePop[1]
        # Determine if node is goal state
        if problem.isGoalState(currNode):
            return pathStart
        else:
            # if node not visited, add to set
            if currNode not in setOfVisited:
                setOfVisited.add(currNode)
                # get successor nodes
                successors = problem.getSuccessors(currNode)
                # iterate through successor nodes
                for succNode in successors:
                    # break list into parts [(nextNode,pathtoNext,cost)]
                    child = succNode[0]
                    pathCurrChild = succNode[1]
                    # add path to cummulative path
                    cummulativePath = pathStart + [pathCurrChild]
                    # push to fringeStack
                    fringeStack.push((child,cummulativePath))
    return pathStart
    util.raiseNotDefined()
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # get Pacman's start position
    start = problem.getStartState()
    # verify that start is not the goal state, if so return empty moves array
    if problem.isGoalState(start):
        return []
    # initialize queue that will be used for the fringe
    fringeQueue = util.Queue()
    # initialize the set that holds the visited nodes (set since no repeats)
    setOfVisited = set()
    # push list of (currNode, pathToCurr) to queue
    fringeQueue.push((start, []))
    # while loop that iterates until stack is empty
    while not fringeQueue.isEmpty():
        # pop from fringeQueue (currNode, pathToCurr)
        nodePop = fringeQueue.pop()
        # break up list into individual elements
        currNode = nodePop[0]
        pathStart = nodePop[1]
        # Determine if node is goal state
        if problem.isGoalState(currNode):
            return pathStart
        else:
            # if node not visited, add to set
            if currNode not in setOfVisited:
                setOfVisited.add(currNode)
                # get successor nodes
                successors = problem.getSuccessors(currNode)
                # iterate through successor nodes
                for succNode in successors:
                    # break list into parts [(nextNode,pathtoNext,cost)]
                    child = succNode[0]
                    pathCurrChild = succNode[1]
                    # add path to cummulative path
                    cummulativePath = pathStart + [pathCurrChild]
                    # push to fringeQueue
                    fringeQueue.push((child,cummulativePath))
    return pathStart
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # get Pacman's start position
    start = problem.getStartState()
    # verify that start is not the goal state, if so return empty moves array
    if problem.isGoalState(start):
        return []
    # initialize priority queue that will be used for the fringe
    fringePQueue = util.PriorityQueue()
    # initialize the set that holds the visited nodes (set since no repeats)
    setOfVisited = set()
    # push list of (currNode, pathToCurr, costToCurr), priority to queue where init path and cost are zero
    fringePQueue.push((start, [], 0), 0)
    # while loop that iterates until stack is empty
    while not fringePQueue.isEmpty():
        # pop from fringePQueue (currNode, pathToCurr, costToCurr)
        nodePop = fringePQueue.pop()
        # break up list into individual elements
        currNode = nodePop[0]
        pathStart = nodePop[1]
        costStart = nodePop[2]
        # Determine if node is goal state
        if problem.isGoalState(currNode):
            return pathStart
        else:
            # if node not visited, add to set
            if currNode not in setOfVisited:
                setOfVisited.add(currNode)
                # get successor nodes
                successors = problem.getSuccessors(currNode)
                # iterate through successor nodes
                for succNode in successors:
                    # break list into parts [(nextNode,pathtoNext,cost)]
                    child = succNode[0]
                    pathCurrChild = succNode[1]
                    costCurrChild = succNode[2]
                    # add path to cummulative path
                    cummulativePath = pathStart + [pathCurrChild]
                    # add cost to cummulative cost
                    cummulativeCost = costStart + costCurrChild
                    # push to fringePQueue with priority of cummulativeCost
                    fringePQueue.push((child,cummulativePath,cummulativeCost),cummulativeCost)
    return pathStart
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # from manhattanHeuristic -> manhattanHeuristic(position, problem, info={})
    # get Pacman's start position
    start = problem.getStartState()
    # verify that start is not the goal state, if so return empty moves array
    if problem.isGoalState(start):
        return []
    # initialize priority queue that will be used for the fringe
    fringePQueue = util.PriorityQueue()
    # initialize the set that holds the visited nodes (set since no repeats)
    setOfVisited = set()
    # get initial heuristic value
    heuristicVal = heuristic(start, problem)
    # push list of (currNode, pathToCurr, costToCurr), priority is heuristic + cost
    fringePQueue.push((start, [], 0), heuristicVal)
    # while loop that iterates until stack is empty
    while not fringePQueue.isEmpty():
        # pop from fringePQueue (currNode, pathToCurr)
        nodePop = fringePQueue.pop()
        # break up list into individual elements
        currNode = nodePop[0]
        pathStart = nodePop[1]
        costStart = nodePop[2]
        # Determine if node is goal state
        if problem.isGoalState(currNode):
            return pathStart
        else:
            # if node not visited, add to set
            if currNode not in setOfVisited:
                setOfVisited.add(currNode)
                # get successor nodes
                successors = problem.getSuccessors(currNode)
                # iterate through successor nodes
                for succNode in successors:
                    # break list into parts [(nextNode,pathtoNext,cost)]
                    child = succNode[0]
                    pathCurrChild = succNode[1]
                    costCurrChild = succNode[2]
                    # fetch heuristic from current sucessor node
                    heuristicCurr = heuristic(child,problem)
                    # add path to cummulative path
                    cummulativePath = pathStart + [pathCurrChild]
                    #add cost to cummulative cost
                    cummulativeCost = costStart + costCurrChild
                    # push to fringePQueue with priority of cummulativeCost + heuristic
                    fringePQueue.push((child,cummulativePath,cummulativeCost), cummulativeCost + heuristicCurr)
    return pathStart
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
