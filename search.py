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

from custom_types import Direction
from pacman import GameState
from typing import Any, Tuple,List
import util

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self)->Any:
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state:Any)->bool:
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state:Any)->List[Tuple[Any,Direction,int]]:
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions:List[Direction])->int:
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()



def tinyMazeSearch(problem:SearchProblem)->List[Direction]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem:SearchProblem)->List[Direction]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    '''
        INSÉREZ VOTRE SOLUTION À LA QUESTION 1 ICI
    '''
    fringe = util.Stack()
    visited = set()

    start = problem.getStartState()
    fringe.push((start, []))  

    while not fringe.isEmpty():
        state, path = fringe.pop()

        if problem.isGoalState(state):
            return path

        if state not in visited:
            visited.add(state)

            for successor, action, cost in problem.getSuccessors(state):
                if successor not in visited:
                    fringe.push((successor, path + [action]))

    return []



def breadthFirstSearch(problem:SearchProblem)->List[Direction]:
    """Search the shallowest nodes in the search tree first."""


    '''
        INSÉREZ VOTRE SOLUTION À LA QUESTION 2 ICI
    '''
    fringe = util.Queue()
    visited = set()

    start = problem.getStartState()
    fringe.push((start, []))  

    while not fringe.isEmpty():
        state, path = fringe.pop()

        if problem.isGoalState(state):
            return path

        if state not in visited:
            visited.add(state)

            for successor, action, cost in problem.getSuccessors(state):
                if successor not in visited:
                    fringe.push((successor, path + [action]))

    return []

def uniformCostSearch(problem:SearchProblem)->List[Direction]:
    """Search the node of least total cost first."""


    '''
        INSÉREZ VOTRE SOLUTION À LA QUESTION 3 ICI
    '''
    fringe = util.PriorityQueue()
    start = problem.getStartState()

    fringe.push((start, [], 0), 0)

    # best known cost to each state
    best_cost = {start: 0}

    while not fringe.isEmpty():
        state, path, current_cost = fringe.pop()

        if state not in best_cost or current_cost != best_cost[state]:
            continue

        if problem.isGoalState(state):
            return path

        for successor, action, cost in problem.getSuccessors(state):
            new_cost = current_cost + cost

            if successor not in best_cost or new_cost < best_cost[successor]:
                best_cost[successor] = new_cost
                fringe.push((successor, path + [action], new_cost), new_cost)

    return []

def nullHeuristic(state:GameState, problem:SearchProblem=None)->List[Direction]:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem:SearchProblem, heuristic=nullHeuristic)->List[Direction]:
    """Search the node that has the lowest combined cost and heuristic first."""
    '''
        INSÉREZ VOTRE SOLUTION À LA QUESTION 4 ICI
    '''
    fringe = util.PriorityQueue()
    start = problem.getStartState()

    start_h = heuristic(start, problem)
    fringe.push((start, [], 0), 0 + start_h)

    best_cost = {start: 0}

    while not fringe.isEmpty():
        state, path, g_cost = fringe.pop()

        if state not in best_cost or g_cost != best_cost[state]:
            continue

        if problem.isGoalState(state):
            return path

        for successor, action, cost in problem.getSuccessors(state):
            new_g = g_cost + cost

            if successor not in best_cost or new_g < best_cost[successor]:
                best_cost[successor] = new_g
                f = new_g + heuristic(successor, problem)
                fringe.push((successor, path + [action], new_g), f)

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
