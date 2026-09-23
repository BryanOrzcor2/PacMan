"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util
import os
import time

def registrar_resultado(algoritmo, heuristica_nombre, problema_nombre, costo, longitud, expandidos, tiempo, acciones):
    """
    Guarda los resultados experimentales en 'resultados_experimentales.log' y 'resultados.csv'.
    """
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    
    # 1. Registro detallado en archivo .log
    log_texto = (
        "==================================================\n"
        "Fecha y Hora:           %s\n"
        "Algoritmo:              %s\n"
        "Heuristica:             %s\n"
        "Problema:               %s\n"
        "Costo del camino (g):   %d\n"
        "Longitud del camino:    %d pasos\n"
        "Nodos expandidos:       %d\n"
        "Tiempo de busqueda:     %.5f s\n"
        "Ruta encontrada:        %s\n"
        "==================================================\n\n" %
        (timestamp, algoritmo, heuristica_nombre, problema_nombre, costo, longitud, expandidos, tiempo, str(acciones))
    )
    with open("resultados_experimentales.log", "a", encoding="utf-8") as f_log:
        f_log.write(log_texto)
        
    # 2. Registro tabular en resultados.csv (archivo del entregable formal)
    csv_file = "resultados.csv"
    existe = os.path.exists(csv_file)
    with open(csv_file, "a", encoding="utf-8") as f_csv:
        if not existe:
            f_csv.write("fecha,algoritmo,heuristica,problema,costo,longitud,nodos_expandidos,tiempo_segundos\n")
        f_csv.write("%s,%s,%s,%s,%d,%d,%d,%.5f\n" % 
                    (timestamp, algoritmo, heuristica_nombre, problema_nombre, costo, longitud, expandidos, tiempo))

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
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  frontera = util.Queue()
  inicio = problem.getStartState()
  frontera.push((inicio, []))
  visitados = set([inicio])

  while not frontera.isEmpty():
    actual, acciones = frontera.pop()
    if problem.isGoalState(actual):
      return acciones
    for sucesor, accion, costo in problem.getSuccessors(actual):
      if sucesor not in visitados:
        visitados.add(sucesor)
        frontera.push((sucesor, acciones + [accion]))
  return []
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  return aStarSearch(problem, heuristic=nullHeuristic, nombre_alg="UCS")

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic, nombre_alg="A*"):
  "Search the node that has the lowest combined cost and heuristic first."
  import time
  t_inicio = time.time()

  # 1. Utilizar una cola de prioridad
  frontera = util.PriorityQueue()

  # 2. Comenzar desde problem.getStartState()
  inicio = problem.getStartState()
  h_inicio = heuristic(inicio, problem)
  frontera.push((inicio, [], 0), 0 + h_inicio)

  # 7. Evitar expansiones innecesarias (registrar el menor costo g conocido)
  mejor_g = {}
  paso = 0

  print("\n--- INICIO DE BUSQUEDA A* ---")
  print("Estado Inicial: %s | Heuristica Inicial h: %s\n" % (str(inicio), str(h_inicio)))

  while not frontera.isEmpty():
    actual, acciones, g_actual = frontera.pop()

    # 7. Descartar caminos obsoletos si ya visitamos este estado con menor o igual costo
    if actual in mejor_g and mejor_g[actual] <= g_actual:
      continue
    mejor_g[actual] = g_actual
    paso += 1

    h_actual = heuristic(actual, problem)
    f_actual = g_actual + h_actual

    # Log pedagogico de expansion de cada nodo
    print("[A* Paso %02d] Casilla: %s | g: %d | h: %d | f=g+h: %d | Nodos en cola: %d" % 
          (paso, str(actual), g_actual, h_actual, f_actual, len(frontera.heap)))

    # 3. Utilizar problem.isGoalState() (Verificacion de meta al extraer - Late Goal Test)
    if problem.isGoalState(actual):
      t_total = time.time() - t_inicio
      heur_nombre = getattr(heuristic, '__name__', str(heuristic))
      prob_nombre = problem.__class__.__name__

      # Registrar en .log y .csv
      registrar_resultado(nombre_alg, heur_nombre, prob_nombre, g_actual, len(acciones), paso, t_total, acciones)

      print("\n" + "="*50)
      print("       RESULTADOS EXPERIMENTALES")
      print("="*50)
      print("  - Costo del camino:     %d" % g_actual)
      print("  - Longitud del camino:  %d" % len(acciones))
      print("  - Nodos expandidos:     %d" % paso)
      print("  - Tiempo de busqueda:   %.4f s" % t_total)
      print("  - Guardado en:          resultados_experimentales.log & resultados.csv")
      print("="*50 + "\n")
      # 8. Retornar una lista de acciones
      return acciones

    # 4. Obtener sucesores mediante problem.getSuccessors()
    for sucesor, accion, costo_paso in problem.getSuccessors(actual):
      # 5. Acumular el costo g(n)
      nuevo_g = g_actual + costo_paso

      # 7. Solo consideramos el sucesor si no ha sido visitado o si encontramos un camino mas barato
      if sucesor not in mejor_g or nuevo_g < mejor_g[sucesor]:
        # 6. Calcular la prioridad g(n) + h(n)
        f = nuevo_g + heuristic(sucesor, problem)
        frontera.push((sucesor, acciones + [accion], nuevo_g), f)

  return []
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch