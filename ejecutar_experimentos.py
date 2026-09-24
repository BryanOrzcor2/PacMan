#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ejecutar_experimentos.py
Capa experimental dedicada para ejecutar y registrar el benchmark
del Taller 3 (Puntos 1, 3, 4, 10 y 11) sin introducir efectos secundarios
en el modulo central de algoritmos (search.py).
"""

import time
import os
import util
import search
import searchAgents
import layout
from pacman import GameState

def registrar_en_csv_y_log(datos, log_file="resultados_experimentales.log", csv_file="resultados.csv"):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    
    # 1. Archivo .log detallado
    log_entry = (
        "==================================================\n"
        "Fecha y Hora:           %s\n"
        "Algoritmo:              %s\n"
        "Heuristica:             %s\n"
        "Problema / Layout:      %s\n"
        "Costo del camino (g):   %d\n"
        "Longitud del camino:    %d pasos\n"
        "Nodos expandidos:       %d\n"
        "Tiempo de busqueda:     %.5f s\n"
        "==================================================\n\n" %
        (timestamp, datos['algoritmo'], datos['heuristica'], datos['layout'],
         datos['costo'], datos['longitud'], datos['expandidos'], datos['tiempo'])
    )
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry)
        
    # 2. Archivo .csv
    existe = os.path.exists(csv_file)
    with open(csv_file, "a", encoding="utf-8") as f:
        if not existe:
            f.write("fecha,algoritmo,heuristica,problema,costo,longitud,nodos_expandidos,tiempo_segundos\n")
        f.write("%s,%s,%s,%s,%d,%d,%d,%.5f\n" %
                (timestamp, datos['algoritmo'], datos['heuristica'], datos['layout'],
                 datos['costo'], datos['longitud'], datos['expandidos'], datos['tiempo']))

def ejecutar_benchmark():
    print("=" * 60)
    print(" EJECUCION DE BENCHMARK EXPERIMENTAL - TALLER 3 PACMAN")
    print("=" * 60)
    
    # Configuraciones de prueba
    experimentos = [
        {"layout": "mediumMaze", "tipo": "position", "alg": search.uniformCostSearch, "heur": search.nullHeuristic, "nombre_alg": "UCS", "nombre_heur": "nullHeuristic"},
        {"layout": "mediumMaze", "tipo": "position", "alg": search.aStarSearch, "heur": search.nullHeuristic, "nombre_alg": "A*", "nombre_heur": "nullHeuristic (h=0)"},
        {"layout": "mediumMaze", "tipo": "position", "alg": search.aStarSearch, "heur": searchAgents.manhattanHeuristic, "nombre_alg": "A*", "nombre_heur": "manhattanHeuristic"},
        {"layout": "mediumMaze", "tipo": "position", "alg": search.aStarSearch, "heur": searchAgents.euclideanHeuristic, "nombre_alg": "A*", "nombre_heur": "euclideanHeuristic"},
        {"layout": "tinyCorners", "tipo": "corners", "alg": search.aStarSearch, "heur": searchAgents.cornersHeuristic, "nombre_alg": "A*", "nombre_heur": "cornersHeuristic"},
        {"layout": "tinyCorners", "tipo": "food_manhattan", "alg": search.aStarSearch, "heur": searchAgents.foodHeuristicManhattan, "nombre_alg": "A*", "nombre_heur": "foodHeuristicManhattan"},
        {"layout": "tinyCorners", "tipo": "food_mst", "alg": search.aStarSearch, "heur": searchAgents.foodHeuristic, "nombre_alg": "A*", "nombre_heur": "foodHeuristic (MST)"},
    ]

    for exp in experimentos:
        lay = layout.getLayout(exp['layout'])
        state = GameState()
        state.initialize(lay, 0)

        if exp['tipo'] == 'position':
            problem = searchAgents.PositionSearchProblem(state, warn=False)
        elif exp['tipo'] == 'corners':
            problem = searchAgents.CornersProblem(state)
        elif exp['tipo'] in ['food_manhattan', 'food_mst']:
            problem = searchAgents.FoodSearchProblem(state)

        t0 = time.time()
        if exp['nombre_alg'] == "UCS":
            actions = exp['alg'](problem)
        else:
            actions = exp['alg'](problem, exp['heur'])
        t1 = time.time()

        costo = problem.getCostOfActions(actions)
        longitud = len(actions)
        expandidos = getattr(problem, '_expanded', len(actions))
        tiempo = t1 - t0

        datos = {
            'algoritmo': exp['nombre_alg'],
            'heuristica': exp['nombre_heur'],
            'layout': exp['layout'],
            'costo': costo,
            'longitud': longitud,
            'expandidos': expandidos,
            'tiempo': tiempo
        }

        print("[OK] %s + %s sobre %s -> Costo: %d | Pasos: %d | Tiempo: %.4f s" %
              (exp['nombre_alg'], exp['nombre_heur'], exp['layout'], costo, longitud, tiempo))
        
        registrar_en_csv_y_log(datos)

    print("\nBenchmark completado. Registros guardados en 'resultados.csv' y 'resultados_experimentales.log'.")

if __name__ == '__main__':
    ejecutar_benchmark()
