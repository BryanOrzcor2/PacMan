# Pacman AI - Algoritmos de Búsqueda Informada (A*)

Implementación de algoritmos de búsqueda clásica e informada para el entorno de Pacman (UC Berkeley AI).

**Asignatura:** Inteligencia Artificial  
**Docente:** Joaquín F. Sánchez  
**Programa:** Maestría en Inteligencia Artificial  
**Institución:** Universidad Sergio Arboleda  

### 👥 Integrantes:
- **Santiago Rodríguez Palacio**
- **Juan José Segura Flórez**
- **Bryan Orozco Romero**

---

## 📋 Requisitos

- **Python 3.x**
- Tkinter (incluido por defecto en la mayoría de instalaciones de Python para la interfaz gráfica).

---

## 🕹️ Modo de Juego Manual

Podés controlar a Pacman manualmente con las flechas del teclado:

```bash
python pacman.py
```

Opciones útiles de tablero y zoom:
```bash
python pacman.py --layout smallClassic --zoom 2
```

---

## 🚀 Ejecución de Agentes de Búsqueda

Para ejecutar a Pacman controlado por un agente de búsqueda (`SearchAgent`), utilizá la bandera `-p SearchAgent` y pasá los argumentos con `-a`.

### 1. Uniform Cost Search (UCS)

Encuentra el camino de menor costo al objetivo:

```bash
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
```

```bash
python pacman.py -l bigMaze -p SearchAgent -a fn=ucs -z 0.5
```

---

### 2. A* Search (A-Estrella)

Utiliza costo acumulado más una función heurística:

#### Con heurística de Manhattan:
```bash
python pacman.py -l bigMaze -z 0.5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

#### Con heurística Euclidiana:
```bash
python pacman.py -l bigMaze -z 0.5 -p SearchAgent -a fn=astar,heuristic=euclideanHeuristic
```

---

### 3. Problema de las 4 Esquinas (Corners Problem)

Encuentra el camino más corto para tocar las cuatro esquinas del mapa:

```bash
# Con Búsqueda en Anchura (BFS)
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

# Con A* y heurística personalizada
python pacman.py -l mediumCorners -p SearchAgent -a fn=astar,prob=CornersProblem,heuristic=cornersHeuristic
```

---

### 4. Comer toda la comida (Food Search Problem)

Encuentra una ruta óptima para recolectar toda la comida del laberinto:

```bash
python pacman.py -l trickyClassic -p SearchAgent -a fn=astar,prob=FoodSearchProblem,heuristic=foodHeuristic
```

---

## ⚙️ Parámetros y Opciones Comunes

| Parámetro | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `-l`, `--layout` | Laberinto/mapa a cargar (ubicados en `layouts/`) | `-l tinyMaze`, `-l mediumMaze`, `-l bigMaze` |
| `-p`, `--pacman` | Tipo de agente para controlar a Pacman | `-p SearchAgent`, `-p KeyboardAgent` |
| `-a`, `--agentArgs` | Argumentos del agente (función `fn`, problema `prob`, heurística `heuristic`) | `-a fn=astar,heuristic=manhattanHeuristic` |
| `-z`, `--zoom` | Escala de zoom de la ventana gráfica | `-z 0.5`, `-z 2` |
| `--frameTime` | Tiempo de espera entre pasos (velocidad de animación) | `--frameTime 0.05` (más rápido), `--frameTime 0` (instantáneo) |
| `-t`, `--textGraphics` | Modo solo texto (sin ventana gráfica) | `-t` |
| `-q`, `--quietTextGraphics` | Salida mínima en terminal sin gráficos | `-q` |

---

## 📂 Archivos Entregables del Taller

- `search.py`: Implementación de los algoritmos de búsqueda ($A^*$, BFS, UCS) con control de visitados `mejor_g` y prueba de meta tardía (*late goal test*).
- `searchAgents.py`: Implementación de `CornersProblem`, `cornersHeuristic` (TSP), `foodHeuristicManhattan` y `foodHeuristic` (Árbol de Expansión Mínima MST con memoria caché).
- `resultados.csv`: Consolidado formal de métricas experimentales exigido por la guía.
- `resultados_experimentales.log`: Traza detallada de ejecución con costos, expansiones y rutas.
- `informe.tex`: Documento en LaTeX con el desarrollo conceptual, matemático y experimental completo (Actividades 1 a 11).