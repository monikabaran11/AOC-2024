grid = []

with open('AOC6.txt', 'r') as file:
    for line in file:
        row=list(line.strip())
        grid.append(row)

print(grid)
print(len(grid)) # number of list in list will give number of rows.
print(len(grid[0])) # first row checking len of the first row will give number of columns

def guard_position_check(grid):
  for row in grid:
      for element in row:
          if element == "^":
            position=(grid.index(row),row.index(element))
            return(position)

position=guard_position_check(grid) # place where guarad is now marked as ^
print(position)
list_of_positions = []
list_of_positions.append(position)

directions = [(-1,0),(0,1),(1,0),(0,-1)]
current_direction = 0
position = (position[0] + directions[current_direction][0],
            position[1] + directions[current_direction][1])  # first place visited by gurad on grid

while position[0] >= 0 and position[0] < len(grid) and position[1] >= 0 and position[1] < len(grid[0]):

    if grid[position[0]][position[1]] == '.' or grid[position[0]][position[1]] == '^':
        list_of_positions.append(position)
        grid[position[0]][position[1]] = 'X'
        position = (position[0] + directions[current_direction][0], position[1] + directions[current_direction][1])
    elif grid[position[0]][position[1]] == 'X':
        position = (position[0] + directions[current_direction][0], position[1] + directions[current_direction][1])
    elif grid[position[0]][position[1]] == '#':
        position = (position[0] - directions[current_direction][0], position[1] - directions[current_direction][1])
        current_direction = ((current_direction + 1) % 4)

    else:
        break

print(list_of_positions)

print(f"Pozycja: {position}, Kierunek: {current_direction}")
print(len(list_of_positions))
count = len(set(list_of_positions))
print(count)