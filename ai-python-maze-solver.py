# Python Maze Solver using A* Algorithm with Movement Constraints
# Author: Aleksi Bovellan (2024)

"""
Movement Constraints:

- At each step, the AI can only:
  - Move forward.
  - Turn right and then move forward.
  
- The AI can't:
  - Turn left.
  - Move backward.
  - Turn in place without moving.

While the script solves the maze it print-outs its movements, and finally also visualizes the found path.
"""

# Import necessary libraries
import matplotlib.pyplot as plt
import time
from matplotlib.collections import LineCollection
import numpy as np

class Node:
    """A node class for A* Pathfinding with orientation."""

    def __init__(self, parent=None, position=None, direction=None, action=None):
        self.parent = parent
        self.position = position
        self.direction = direction  # Direction: 'up', 'down', 'left', 'right'
        self.action = action        # Action taken to reach this node

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position and self.direction == other.direction

def get_new_direction(current_direction, turn):
    """Get the new direction based on the current direction and the turn ('forward' or 'right')."""
    directions = ['up', 'right', 'down', 'left']
    current_index = directions.index(current_direction)
    if turn == 'right':
        new_index = (current_index + 1) % 4
    else:  # forward
        new_index = current_index
    return directions[new_index]

def get_new_position(current_position, direction):
    """Get the new position based on the current position and direction."""
    movement = {
        'up': (-1, 0),    # Move up (decrease row index)
        'down': (1, 0),   # Move down (increase row index)
        'left': (0, -1),  # Move left (decrease column index)
        'right': (0, 1)   # Move right (increase column index)
    }
    move = movement[direction]
    return (current_position[0] + move[0], current_position[1] + move[1])

def astar(maze, start, end):
    """Returns a list of positions as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_direction = 'up'  # Assuming the agent starts facing 'up'
    start_node = Node(None, start, start_direction, action='Start')
    end_node = Node(None, end, None)

    # Initialize both open and closed lists
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while open_list:

        # Get the node with the lowest f score
        current_node = min(open_list, key=lambda node: node.f)
        open_list.remove(current_node)
        closed_list.append(current_node)

        # Print current state
        print(f"Current position: {current_node.position}, Orientation: {current_node.direction}, Action: {current_node.action}")

        # Found the goal
        if current_node.position == end_node.position:
            path = []
            current = current_node
            while current:
                path.append((current.position, current.direction, current.action))
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []

        # Possible actions from the current node
        possible_actions = []

        # Action 1: Move forward
        new_direction = current_node.direction
        new_position = get_new_position(current_node.position, new_direction)
        if 0 <= new_position[0] < len(maze) and 0 <= new_position[1] < len(maze[0]):
            if maze[new_position[0]][new_position[1]] == 0:
                forward_node = Node(current_node, new_position, new_direction, action='Move Forward')
                children.append(forward_node)
                possible_actions.append(f"Move Forward to {new_position}, Orientation: {new_direction}")

        # Action 2: Turn right and move forward
        new_direction_right = get_new_direction(current_node.direction, 'right')
        new_position_right = get_new_position(current_node.position, new_direction_right)
        if 0 <= new_position_right[0] < len(maze) and 0 <= new_position_right[1] < len(maze[0]):
            if maze[new_position_right[0]][new_position_right[1]] == 0:
                right_node = Node(current_node, new_position_right, new_direction_right, action='Turn Right and Move Forward')
                children.append(right_node)
                possible_actions.append(f"Turn Right and Move Forward to {new_position_right}, Orientation: {new_direction_right}")

        # Print possible next actions
        for action in possible_actions:
            print(f" -> Next action: {action}")

        # Loop through children
        for child in children:

            # Child is on the closed list
            if any(closed_child for closed_child in closed_list if closed_child == child):
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1  # Each move has a cost of 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            existing_node = next((open_node for open_node in open_list if open_node == child), None)
            if existing_node and child.g >= existing_node.g:
                continue
            else:
                open_list.append(child)

        # Small delay for readability
        time.sleep(0.1)
        print("")  # Empty line for better readability

def visualize_maze(maze, path, start, end):
    """Visualizes the maze and the path taken by the agent with a gradient color."""
    plt.imshow(maze, cmap='binary')  # By default, origin='upper'
    y_path, x_path = zip(*[step[0] for step in path])

    # Create a list of points
    points = np.array([x_path, y_path]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    # Create a LineCollection from the segments
    lc = LineCollection(segments, cmap='magma', linewidth=3)
    lc.set_array(np.linspace(0, 1, len(segments)))

    # Add the LineCollection to the plot
    plt.gca().add_collection(lc)

    # Plot the start and end points
    plt.scatter([start[1]], [start[0]], color='green', s=100, label='Start')
    plt.scatter([end[1]], [end[0]], color='blue', s=100, label='End')
    plt.title('Maze Solution Path with Gradient')
    plt.legend()
    plt.colorbar(lc, label='Path Progression')
    plt.show()

def main():
    # The maze
    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 0 (top)
            [0, 1, 0, 1, 0 ,1, 1, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0 ,1, 1, 1, 1, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
            [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]]  # Row 11 (bottom)

    start = (11, 10)  # Starting position at the bottom (row 11)
    end = (11, 2)     # Ending position at the bottom (row 11)

    print("Starting A* algorithm with movement constraints...\n")
    path = astar(maze, start, end)

    if path:
        print("\nPath found:")
        for pos, direction, action in path:
            print(f"Position: {pos}, Orientation: {direction}, Action: {action}")
            time.sleep(0.1)

        # Visualize the maze and path
        visualize_maze(maze, path, start, end)
    else:
        print("No path found.")

if __name__ == '__main__':
    main()
