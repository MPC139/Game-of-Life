import random
import time
import copy
import os

WIDTH = 60
HEIGHT = 20

# print the grid
def print_grid(grid):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(grid[x][y], end='')
        print()

next_grid = []
for x in range(WIDTH):
    aux = []
    for y in range(HEIGHT):
        if random.randint(0, 1):
            aux.append('#')
        else:
            aux.append(' ')
    next_grid.append(aux)

left_indices = [(y - 1) % HEIGHT for y in range(HEIGHT)]
right_indices = [(y + 1) % HEIGHT for y in range(HEIGHT)]
up_indices = [(x - 1) % WIDTH for x in range(WIDTH)]
below_indices = [(x + 1) % WIDTH for x in range(WIDTH)]
import random  # Importing the random module for generating random values
import time  # Importing the time module for introducing delays
import copy  # Importing the copy module for creating deep copies of objects
import os  # Importing the os module for interacting with the operating system

WIDTH = 60  # Width of the grid
HEIGHT = 20  # Height of the grid

# Function to print the grid
def print_grid(grid):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(grid[x][y], end='')  # Printing each cell of the grid
        print()  # Printing a new line after each row

next_grid = []  # List to store the next state of the grid
for x in range(WIDTH):
    aux = []
    for y in range(HEIGHT):
        if random.randint(0, 1):
            aux.append('#')  # Randomly assigning '#' to represent an alive cell
        else:
            aux.append(' ')  # Assigning ' ' to represent a dead cell
    next_grid.append(aux)

left_indices = [(y - 1) % HEIGHT for y in range(HEIGHT)]  # Indices of left neighboring cells
right_indices = [(y + 1) % HEIGHT for y in range(HEIGHT)]  # Indices of right neighboring cells
up_indices = [(x - 1) % WIDTH for x in range(WIDTH)]  # Indices of upper neighboring cells
below_indices = [(x + 1) % WIDTH for x in range(WIDTH)]  # Indices of lower neighboring cells

while True:
    current_grid = copy.deepcopy(next_grid)  # Creating a deep copy of the next grid state
    print_grid(current_grid)  # Printing the current state of the grid
    for x in range(WIDTH):
        for y in range(HEIGHT):
            left = left_indices[y]
            right = right_indices[y]
            up = up_indices[x]
            below = below_indices[x]
            cont = 0  # Counter for counting the number of alive neighbors

            # Checking the state of each neighboring cell and incrementing the counter if it is alive
            if current_grid[x][left] == '#':
                cont += 1
            if current_grid[x][right] == '#':
                cont += 1 
            if current_grid[up][left] == '#':
                cont += 1
            if current_grid[up][y] == '#':
                cont += 1
            if current_grid[up][right] == '#':
                cont += 1
            if current_grid[below][left] == '#':
                cont += 1
            if current_grid[below][y] == '#':
                cont += 1
            if current_grid[below][right] == '#':
                cont += 1

            # Applying the rules of the Game of Life to determine the next state of the cell
            if current_grid[x][y] == '#' and cont in (2, 3):
                next_grid[x][y] = '#'  # Cell remains alive
            elif current_grid[x][y] == ' ' and cont == 3:
                next_grid[x][y] = '#'  # Cell becomes alive
            else:
                next_grid[x][y] = ' '  # Cell remains dead

    time.sleep(1)  # Introducing a delay of 1 second
    os.system('clear')  # Clearing the console screen to create the animation effect