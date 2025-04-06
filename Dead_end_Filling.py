import tkinter as tk
from time import sleep
import random

def draw_grid(canvas, grid, cell_size):
    """Render the maze grid on the canvas with appropriate colors."""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            if grid[i][j] == 1:  # Wall
                canvas.create_rectangle(x1, y1, x2, y2, fill="black")
            elif grid[i][j] == 2:  # Dead-end
                canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
            else:  # Open path
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")

def highlight_cell(canvas, node, cell_size, color):
    """Highlight a specific cell on the canvas with the given color."""
    x1, y1 = node[1] * cell_size, node[0] * cell_size
    x2, y2 = x1 + cell_size, y1 + cell_size
    canvas.create_rectangle(x1, y1, x2, y2, fill=color)

def generate_maze_with_prim(root, canvas, width, height, cell_size):
    """Generate a maze using the Randomized Prim's algorithm with visualization."""
    grid = [[1 for _ in range(width)] for _ in range(height)]
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
    
    # Starting point
    start_x, start_y = 1, 1
    grid[start_x][start_y] = 0
    walls = [(start_x, start_y, start_x + dx, start_y + dy) 
             for dx, dy in directions 
             if 0 <= start_x + dx < height and 0 <= start_y + dy < width]
    
    while walls:
        x1, y1, x2, y2 = walls.pop(random.randrange(len(walls)))
        if 0 <= x2 < height and 0 <= y2 < width and grid[x2][y2] == 1:
            grid[x2][y2] = 0
            grid[(x1 + x2) // 2][(y1 + y2) // 2] = 0
            highlight_cell(canvas, (x2, y2), cell_size, "orange")
            highlight_cell(canvas, ((x1 + x2) // 2, (y1 + y2) // 2), cell_size, "red")
            root.update()
            sleep(0.001)
            
            walls.extend((x2, y2, x2 + dx, y2 + dy) 
                         for dx, dy in directions 
                         if 0 <= x2 + dx < height and 0 <= y2 + dy < width and grid[x2 + dx][y2 + dy] == 1)
    
    start = (1, 1)
    goal = (height - 2, width - 2)
    grid[start[0]][start[1]] = 0
    grid[goal[0]][goal[1]] = 0
    
    draw_grid(canvas, grid, cell_size)
    root.update()
    
    return grid, start, goal

def dead_end_filling(root, canvas, grid, start, goal, cell_size):
    """Solve the maze using the Dead-End Filling algorithm with visualization."""
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def is_dead_end(x, y):
        """Check if a cell is a dead-end."""
        if grid[x][y] != 0:
            return False
        neighbors = sum(1 for dx, dy in directions 
                        if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] == 0)
        return neighbors == 1 and (x, y) != start and (x, y) != goal
    
    # Fill dead-ends
    while True:
        changed = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if is_dead_end(i, j):
                    grid[i][j] = 2
                    highlight_cell(canvas, (i, j), cell_size, "blue")
                    root.update()
                    sleep(0.005)
                    changed = True
        if not changed:
            break
    
    # Find the solution path
    path = []
    current = start
    visited = set()
    while current != goal:
        visited.add(current)
        x, y = current
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and 
                grid[nx][ny] == 0 and (nx, ny) not in visited):
                path.append(current)
                current = (nx, ny)
                break
        else:
            print("No path found!")
            return
    
    path.append(goal)
    
    # Highlight the solution path
    for node in path:
        highlight_cell(canvas, node, cell_size, "green")
        root.update()
        sleep(0.005)
    
    print("Path found:", path)

def main():
    """Initialize and run the maze generation and solving visualization."""
    root = tk.Tk()
    root.title("Maze Visualization")
    
    # Configuration
    maze_width, maze_height = 101, 101
    cell_size = 5
    canvas_width = 505
    canvas_height = 505
    
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()
    
    grid, start, goal = generate_maze_with_prim(root, canvas, maze_width, maze_height, cell_size)
    dead_end_filling(root, canvas, grid, start, goal, cell_size)
    
    root.mainloop()

if __name__ == "__main__":
    main()
