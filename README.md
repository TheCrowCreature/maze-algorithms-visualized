# 🧩 Maze Algorithms Visualizer

An interactive maze generator and solver built with Python and Tkinter. This project visualizes popular pathfinding and maze generation algorithms like **Prim's Algorithm**, **Dijkstra's Algorithm**, **A\***, and **Dead-End Filling** in real-time with animations.

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/gui-tkinter-green.svg" />
  <img src="https://img.shields.io/badge/algorithms-Prim%20%7C%20Dijkstra%20%7C%20A%2A%20%7C%20Dead--End%20Filling-purple.svg" />
</p>

---

## ✨ Features

- Visualize **maze generation** with [Randomized Prim’s Algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm#Prim's_algorithm)
- Visualize **pathfinding** with:
  - ✅ [Dijkstra’s Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
  - ✅ [A\* Search Algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm)
  - ✅ [Dead-End Filling](https://en.wikipedia.org/wiki/Maze_solving_algorithm#Dead-end_filling)
- Smooth animations using `Tkinter` GUI.
- Color-coded cells:
  - 🟧 Maze generation in progress
  - 🔵 Dead-ends
  - 🟩 Final path
  - 🔴 Maze carving
  - ⚪ Open space
  - ⬛ Walls

---

## 🧠 Algorithms

### 🔨 Maze Generation: Prim's Algorithm
- Starts from a single cell.
- Randomly carves paths to nearby cells.
- Ensures the maze is fully connected without isolated parts.

### 🧭 Dijkstra's Algorithm
- Guarantees the shortest path.
- Expands evenly in all directions from the start point.
- Suitable when all paths have equal cost.

### ⭐ A* Search Algorithm
- Faster than Dijkstra using a heuristic (Euclidean distance).
- Prioritizes paths that look promising toward the goal.

### 🕳️ Dead-End Filling
- A unique solver that removes all dead ends.
- Leaves only the correct solution path from start to end.

---

## 🚀 Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/TheCrowCreature/maze-algorithms-visualizer
   cd maze-algorithms-visualizer
2. Run the Python Files:
    ```bash
    python Dead_end_Filling.py
    python Dijkstra.py
    python A_start.py
