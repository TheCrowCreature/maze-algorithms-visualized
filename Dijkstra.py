import tkinter as tk
from time import sleep
import random
import heapq

def draw_grid(canvas, grid, cell_size):
    """Render the maze grid on the canvas with appropriate colors."""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            if grid[i][j] == 1:  # Wall
                canvas.create_rectangle(x1, y1, x2, y2, fill="black")
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

def dijkstra(root, canvas, grid, start, goal, cell_size):
    """Solve the maze using Dijkstra's algorithm with visualization."""
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Priority queue with (distance, node)
    open_set = [(0, start)]
    came_from = {}
    distances = {start: 0}
    visited = set()
    
    while open_set:
        dist, current = heapq.heappop(open_set)
        
        if current == goal:
            # Reconstruct and highlight the path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path = path[::-1]
            
            for node in path:
                highlight_cell(canvas, node, cell_size, "green")
                root.update()
                sleep(0.005)
            print("Path found:", path)
            return
        
        if current in visited:
            continue
        
        visited.add(current)
        if current != start:  # Avoid overwriting start point
            highlight_cell(canvas, current, cell_size, "blue")  # Visited nodes
            root.update()
            sleep(0.005)
        
        x, y = current
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)
            if (0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and 
                grid[neighbor[0]][neighbor[1]] != 1):
                new_dist = distances[current] + 1
                
                if new_dist < distances.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    distances[neighbor] = new_dist
                    heapq.heappush(open_set, (new_dist, neighbor))
    
    print("No path found!")

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
    dijkstra(root, canvas, grid, start, goal, cell_size)
    
    root.mainloop()

if __name__ == "__main__":
    main()
