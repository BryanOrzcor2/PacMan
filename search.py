"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
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
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Graph search implementation using a LIFO stack.
  """
  frontier = util.Stack()
  start_state = problem.getStartState()
  frontier.push((start_state, []))
  visited = set()

  while not frontier.isEmpty():
    state, actions = frontier.pop()

    if problem.isGoalState(state):
      return actions

    if state in visited:
      continue
    visited.add(state)

    for successor, action, step_cost in problem.getSuccessors(state):
      if successor not in visited:
        frontier.push((successor, actions + [action]))

  return []

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first. [p 81]
  
  Graph search implementation using a FIFO queue.
  """
  frontier = util.Queue()
  start_state = problem.getStartState()
  frontier.push((start_state, []))
  visited = set([start_state])

  while not frontier.isEmpty():
    state, actions = frontier.pop()

    if problem.isGoalState(state):
      return actions

    for successor, action, step_cost in problem.getSuccessors(state):
      if successor not in visited:
        visited.add(successor)
        frontier.push((successor, actions + [action]))

  return []
      
def uniformCostSearch(problem):
  """Search the node of least total cost first."""
  frontier = util.PriorityQueue()
  start_state = problem.getStartState()
  frontier.push((start_state, [], 0), 0)
  visited = set()

  while not frontier.isEmpty():
    state, actions, current_cost = frontier.pop()

    if state in visited:
      continue
    visited.add(state)

    if problem.isGoalState(state):
      return actions

    for successor, action, step_cost in problem.getSuccessors(state):
      if successor not in visited:
        next_cost = current_cost + step_cost
        frontier.push((successor, actions + [action], next_cost), next_cost)

  return []

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  """Search the node that has the lowest combined cost and heuristic first."""
  frontier = util.PriorityQueue()
  start_state = problem.getStartState()
  frontier.push((start_state, [], 0), heuristic(start_state, problem))
  visited = set()

  while not frontier.isEmpty():
    state, actions, current_cost = frontier.pop()

    if state in visited:
      continue
    visited.add(state)

    if problem.isGoalState(state):
      return actions

    for successor, action, step_cost in problem.getSuccessors(state):
      if successor not in visited:
        next_cost = current_cost + step_cost
        priority = next_cost + heuristic(successor, problem)
        frontier.push((successor, actions + [action], next_cost), priority)

  return []
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch