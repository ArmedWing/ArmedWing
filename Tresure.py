import os
os.system('cls||clear') # this is to clear the terminal after every run of the program

print("Hello there traveler! There is a tresure hidden on the map! It is yours, if you can find it!\nI will give you a little hint: It's from a famous quote from Hamlet!\n")

# Making the grid
def display_game(game, grid_size):    # Defining a function. game is the strings that represent the cells in the grid, whilst the grid_size represents the size of the grid
    header_row = ' '
    row = ''
    for x in range(1,grid_size+1):  # For loop to check the grid size
        header_row = header_row + ' | ' + str(x)  
        row = row + ' | ' + game 
    print(header_row + ' | ')
    print('-' * (len(row)+3))
    char = 64
    for x in range(1,grid_size+1): # Another for loop
        char = char  +1 
        print(chr(char) + row + ' | ')
        print('-' * (len(row)+3))

display_game(' ', 4)   # Changing the number will make the grid bigger (6 would be 6x6 grid)

x = "not_2B"
x = input("\nSelect coordinates to find the treasure: ")  # First input from user
while x != "2B":   # Checking if the input is not 2B (the correct coordiante for the treasure)
    if x != "2B":
        x = input("Tresure not here! Try another coordinate: ")  # If the input is not the correct one, you have to make another try
        
print("You found the treasure! I wonder what it is?") # If the user input 2B, it will end the program saying "You found the treasure"