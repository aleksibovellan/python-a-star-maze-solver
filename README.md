# Python Maze Solver using A* Algorithm with Movement Constraints

**Author:** Aleksi Bovellan (2024)

**Technologies:** Python 3, Matplotlib for visualization


---

![screenshot](https://github.com/user-attachments/assets/d08b4009-b823-4bd0-9d97-5255717c869a)

---

# DESCRIPTION

A Python script with an AI algorithm that solves a 2D maze using the A* search algorithm - but, with specific movement constraints, to force the AI really earn its way out of the maze. This time, after first entering the maze, the AI can only move forward, or turn right and then move forward. It cannot turn left or move backward. The optimal route would be very short with free movement, but this tweak eventually creates probably the longest possible route to the exit point, by having to loop around the maze several times due to turning restrictions by design.

**The idea was to show its problem-solving ability to navigate complex environments even with limited movement options.**

This solver print-outs its steps into the console during runtime, and in the end also creates a graphic image of the maze with the successful path eventually found.

---

# INCLUDED FILES

- `ai-python-maze-solver.py` - The main script containing the maze-solving algorithm and visualization.
- `README.md` - This file with instructions and project details.

---

# PRE-INSTALLATION:

pip install matplotlib

---

# USAGE

python3 ai-python-maze-solver.py

---

# MOVEMENT CONSTRAINTS

- **Allowed Actions:**
  - **Move Forward:** The agent moves one cell forward in the direction it is currently facing.
  - **Turn Right and Move Forward:** The agent turns 90 degrees to the right and then moves one cell forward in the new direction.

- **Disallowed Actions:**
  - **Turn Left**
  - **Move Backward**
  - **Turn in Place Without Moving**

---

# A* SEARCH ALGORITHM

The A* algorithm is used to find the optimal path from the start to the end point within the maze, considering the movement constraints.

- **Nodes:** Each node represents a state defined by its position and the direction the agent is facing.
- **Open List:** Nodes to be evaluated.
- **Closed List:** Nodes already evaluated.
- **Cost Functions:**
  - **g(n):** The cost to move from the start node to node n.
  - **h(n):** The heuristic estimated cost from node n to the goal (Euclidean distance).
  - **f(n):** Total cost of the node (f(n) = g(n) + h(n)).

# HEURISTIC FUNCTION

- **Euclidean Distance:** Used to estimate the cost from the current node to the goal:

  ```python
  h = (current_node.position[0] - end_node.position[0]) ** 2 + (current_node.position[1] - end_node.position[1]) ** 2
  ```

# MAZE REPRESENTATION

- The maze is a 2D list where:
  - `0` represents a walkable path.
  - `1` represents a wall.

# VISUALIZATION

- **Matplotlib** is used to create a visual representation of the maze and the agent's path.
- The path is plotted over the maze image, with the start point marked in green and the end point in blue:
  - **Walls** are shown in black.
  - **Walkable paths** are shown in white.
  - **Agent's path** is overlaid in red.
  - **Start point** is marked in green.
  - **End point** is marked in blue.

---

# CODE LOGIC

### `Node` Class

Represents each state in the search space.

- **Attributes:**
  - `parent`: Reference to the parent node.
  - `position`: Tuple `(row, column)` indicating the node's position in the maze.
  - `direction`: The agent's facing direction (`'up'`, `'down'`, `'left'`, `'right'`).
  - `g`, `h`, `f`: Cost functions.

### Movement Functions

- **`get_new_direction(current_direction, turn)`**
  - Determines the new direction after turning.
- **`get_new_position(current_position, direction)`**
  - Calculates the new position based on the current position and direction.

### `astar(maze, start, end)` Function

- Implements the A* search algorithm with movement constraints.
- Generates child nodes based on allowed actions.
- Evaluates and selects nodes based on the lowest `f(n)` value.

### `visualize_maze(maze, path, start, end)` Function

- Creates a visual representation of the maze and the agent's path using Matplotlib.
- Plots the maze grid, the path taken, and marks the start and end points.

### `main()` Function

- Defines the maze layout, start, and end positions.
- Calls the `astar` function to find the path.
- Prints the path and visualizes it.

---

# CUSTOMIZATION

- **Maze Layout:**
  - You can modify the `maze` variable in the script to test different mazes.
- **Start and End Positions:**
  - Adjust the `start` and `end` tuples to change the agent's starting and ending points.
- **Movement Constraints:**
  - The movement logic is defined in the `get_new_direction` and `get_new_position` functions. You can modify these to change the agent's allowed movements.

