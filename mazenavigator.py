import curses
from curses import wrapper
import queue
import time         # imports a delay when we start to visualize things
import tracemalloc


# Before running BFS
start_time = time.time()

# Start tracking memory
tracemalloc.start()

# maze = (
#         ["#", "O", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
#         ["#", " ", " ", " ", " ", "#", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#         ["#", " ", "#", "#", " ", "#", "#", " ", "#", " ", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#"],
#         ["#", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", "#", " ", "#"],
#         ["#", " ", "#", " ", "#", " ", "#", "#", "#", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
#         ["#", " ", "#", " ", "#", " ", "#", " ", " ", " ", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
#         ["#", " ", "#", "#", "#", " ", "#", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#", "#", "#", "#"],
#         ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#         ["#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
#         ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#         ["#", " ", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
#         ["#", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#         ["#", " ", "#", " ", "#", "#", "#", " ", "#", " ", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#"],
#         ["#", " ", "#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#         ["#", " ", "#", " ", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
#         ["#", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#         ["#", "#", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
#         ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#         ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "X", "#"],
# )

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", "#", "#", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", " ", "#", " ", "#", "#", "#", " ", "#", " ", "#", " ", "#", " ", "#", "#", "#", " ", " ", "#", " ", "#", " ", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", "#", " ", " ", " ", "#", " ", " ", " ", " ", "#", "#", " ", "#"],
    ["#", " ", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", " ", " ", " ", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", " ", "#"],
    ["#", "#", "#", "#", " ", "#", "#", "#", " ", "#", " ", " ", "#", " ", " ", " ", "#", "#", "#", " ", " ", " ", "#", "#", "#", "#", "#", "#", " ", "#"],
    ["#", "#", "#", " ", " ", "#", " ", "#", " ", "#", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", " ", "#"],
    ["#", "#", "#", " ", "#", "#", " ", "#", " ", "#", "#", "#", "#", " ", "#", "#", " ", " ", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#", "#", " ", "#", "#", " ", " ", " ", " ", "#", "#", "#", "#", "#", " ", " ", " ", " ", "#"],
    ["#", "#", "#", " ", "#", "#", "#", "#", " ", " ", " ", " ", " ", " ", "#", "#", "#", " ", "#", " ", " ", " ", "#", "#", "#", "#", "#", " ", "#", "#"],
    ["#", " ", " ", " ", " ", " ", "#", "#", " ", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", " ", " ", "#", "#", "#", "#", "#", "#", " ", "#", "#"],
    ["#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", " ", " ", " ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " ", " ", "#", "#"],
    ["#", "#", "#", " ", " ", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", " ", " ", " ", " ", " ", " ", " ", "#", "#", "#", "#"],
    ["#", "#", "#", " ", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", " ", "#", " ", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", "#", "#", "#", "#", "#", " ", " ", " ", "#", "#", "#", " ", " ", " ", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", " ", " ", "#", "#", "#", "#", "#", "#", " ", " ", " ", "#", "#"],
    ["#", "#", "#", " ", " ", " ", " ", "#", "#", "#", " ", " ", "#", "#", " ", " ", " ", " ", " ", " ", "#", "#", "#", "#", "#", " ", "#", " ", "#", "#"],
    ["#", "#", "#", " ", " ", "#", " ", "#", "#", "#", " ", " ", " ", "#", " ", " ", " ", " ", "#", " ", "#", "#", "#", "#", "#", " ", "#", " ", "#", "#"],
    ["#", "#", " ", " ", "#", "#", " ", "#", "#", "#", " ", "#", " ", " ", " ", " ", "#", "#", "#", " ", "#", "#", "#", " ", " ", " ", "#", " ", "#", "#"],
    ["#", " ", " ", "#", "#", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#", " ", " ", " ", "#", "#", "#", " ", "#", " ", " ", "#"],
    ["#", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", " ", " ", " ", "#", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#", " ", "#"],
    ["#", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " ", " ", "#", "#", "#", "#", "#", "#", " ", " ", " ", " ", " ", "#", " ", " ", "#"],
    ["#", " ", " ", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", " ", " ", " ", "#", "#"],
    ["#", "#", " ", " ", " ", " ", " ", "#", "#", "#", "#", "#", "#", " ", " ", " ", " ", " ", " ", " ", "#", "#", "#", " ", "#", " ", "#", " ", "#", "#"],
    ["#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", " ", "#", "#", "#", "#", " ", " ", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#", "#", "#", " ", " ", " ", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#", " ", "#", " ", " ", " ", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", " ", "#", "#", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "X", "#", "#", "#", "#"],
]





# maze[6][1] = '#'
# Breadth first search algorithm: Finding shortst path from some starting node to en ending node. The format is a row x column matrix
# (1,1) for ex. We slowly expand path outward by 1 from the starting node and check to see if each neighboring cell(node) 
# is empty or has a obstacle in front of it. And it does this until it reaches the end node. It expands to whichever space it sees available 
# on the grid you have.
# We use a Queue (Q) Data Structure which is a first in first out type of data structure. That means if you enter some item into a Queue
# and its first, it'll be the first item to come out. If you enter an item second, it'll be the second to come out and so on.
# We use this to process elements in the order by which they enter the Queue (Q). 
# We will also have a back and front of Queue (Q)
#Example Queue:
# (3,0) | Front   -   From here we check the neighboring cells if they are the end node and if they are we're done and we found the 
# shortest path. If NOT we add it to the Queue(Q) and then they can be processed and then continue expanding until we find the end node.
# Once elements are processed (3,0) we can add them to a set so we know we already processed that element and continue our search.
# ^^ This is also helpful so that when you move onto a new cell your search algorithm won't search backwards bc it knows you already
# processed that.

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    YELLOW = curses.color_pair(2)

    for i, row in enumerate(maze):      #enumerate gives the i = index as well as the row = value, 1 x row matrix
        for j, value in enumerate(row): #row is your list ov values and j is the column that enumerates over each value and value is the value of each symbol in list 'row'
            if (i, j) in path:
                stdscr.addstr(i, j*3, 'X', YELLOW)
            else:
                stdscr.addstr(i, j*3, value, BLUE)   

def find_start(maze, start):
    # Function that tells us the coordinates of our 'O' start point
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j 
    
    return None

def find_path(maze, stdscr):
    start = 'O'
    end = 'X'
    start_pos = find_start(maze, start)
    
    q = queue.Queue()
    q.put((start_pos, [start_pos]))  #adding 2 elements bc I want to keep track of the pos of the node I want to process next as well as the path to get to that node
                    # ^^ This is puting the two elements [i, j] into a bracket in the queue
    visited = set()
    
    while not q.empty():
        time.sleep(0.01)
        current_pos, path = q.get()    #get the current pos AND==(,) path, which is whatevers at the front of the queue THAT'S WHY PATH+q.get
        row, col = current_pos         # then I'm going to get the current row AND column of the current position to use it in the next functions

        # This allows us to see what the path is doing in real time
        stdscr.clear()
        print_maze(maze, stdscr, path)
        stdscr.refresh()

        if maze[row][col] == end:
            return path, visited
        
        neighbors = find_neighbors(maze, row, col)

        # We check whether neighbor is an obstacle or a cell we have checked already
        for neighbor in neighbors:
            r, c = neighbor
            if maze[r][c] == '#':
                continue            # this is saying skip it if it's a wall
            if neighbor in visited:
                continue                # This is saying if our neighbor cell is in our visited set (the cells we've already processed) continue the search
           
           
            new_path = path + [neighbor]   # What this is doing is tacking the neighbor onto the current path
            q.put((neighbor, new_path))     # This adds these elements to the queue
            visited.add(neighbor)
            #nodes_processed += 1
    
def find_neighbors(maze, row, col):
    neighbors = []

    # This looks UP
    if row > 0:                             #we're saying if row > 0 bc if row = 0 we're at the bounds of our maze so if its 1 or > 0 we check
        neighbors.append((row-1, col))      # This adds the neighbors above w/ the append tool and row - 1. bc our matrix is the top left corner is (0,0)

    # This looks DOWN
    if row + 1 < len(maze):         # This is saying if the row below is less than the length of maze (the bounds) then add it down. If it would've = len(maze) then adding it down would be 'out of maze bounds'
        neighbors.append((row+1, col))

    # This checks LEFT
    if col > 0:
        neighbors.append((row, col - 1))
    
    # This checks RIGHT
    if col + 1 < len(maze[0]):          # This maze[0] means all the elements in the first row (0) which would be the max amt of columns you have
        neighbors.append((row, col + 1))

    return neighbors

def main(stdscr):           #standard output screen - stdscr it overides and takes over terminal
    # Add color
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
  
    mazez = maze

    path, visited = find_path(mazez, stdscr)
    if path:
        final_nodes = 0
        for i in path:
            final_nodes += 1
        print(f"Total Nodes in Final path: {final_nodes}")

        processed_nodes = 0
        for j in visited:
            processed_nodes += 1
        print(f"All processed (visited) nodes: {processed_nodes}")

    #find_path(mazez, stdscr)
 
    stdscr.getch()          #get character, basically if you hit any key in terminal it restarts the terminal
    


wrapper(main)           #this initiallizes the curses module for us and then it calls the function and passes the stdscr object and then we can use that to control our output


# After BFS finishes
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")


# Get memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 10**6:.6f} MB; Peak: {peak / 10**6:.6f} MB")

# Stop tracking
tracemalloc.stop()


