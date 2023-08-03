def process_instructions(instructions, grid_size):
    # Initializing the actual grid position and direction of the rover
    x = 0
    y = 0
    direction = 0  # Rover's direction:
                   # if direction modulo 4 == 0 -> North
                   # if direction modulo 4 == 1 or -3 -> East
                   # if direction modulo 4 == 2 or -2 -> South
                   # if direction modulo 4 == 3 or -1 -> West

    for command in instructions:
        tempx = x  # Temporary x variable to calculate rover's movement along the x-axis
        tempy = y  # Temporary y variable to calculate rover's movement along the y-axis

        if command == 'L':
            direction -= 1
        if command == 'R':
            direction += 1

            direction = direction % 4    #Final direction of the rover

        if (direction == 1 or direction  == -3) and command == 'F':
            tempx += 1
        if (direction == -1 or direction == 3) and command == 'F':
            tempx -= 1
        if direction == 0 and command == 'F':
            tempy += 1
        if (direction == -2 or direction == 2) and command == 'F':
            tempy -= 1

        # Setting the boundary for the rover's movement
        if (0 <= tempx and tempx < grid_size[1]) and (0 <= tempy and tempy < grid_size[0]):
            x = tempx  # If the rover's x movement is within the set boundary, only then it is assigned to the actual x variable
            y = tempy  # If the rover's y movement is within the set boundary, only then it is assigned to the actual y variable

    return x, y, direction

# Taking instruction input for the rover
instructions = input("Enter your instruction to the rover: ")

# Taking grid row and column input and storing it in the grid_size tuple
gridRow, gridCol = map(int, input("Enter grid size: ").split())
grid_size = (gridRow, gridCol)


# Storing the processed tuple which contains the final result
ans = process_instructions(instructions, grid_size)
print(f"Coordinates (x,y): ({ans[0]},{ans[1]})")

# print("Coordinates (x,y):", process_instructions(instructions, grid_size))

#Direction processing
if ans[2] == 0:
    print("Direction: N")
elif ans[2] == 1 or ans[2] == -3:
    print("Direction: E")
elif ans[2] == 2 or ans[2] == -2:
    print("Direction: S")
elif ans[2] == 3 or ans[2] == -1:
    print("Direction: W")