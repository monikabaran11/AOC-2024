grid = []

with open('AOC8.txt', 'r') as file:
    for line in file:
        row=list(line.strip())
        grid.append(row)

print(grid)
print(len(grid)) # row -number of list in list will give number of rows.
print(len(grid[0])) # column- first list checking len of the first row will give number of columns
anten_set=set()
anten_dict={}
antinodes_set=set()
antinodes_lst=[]
antinodes_ingrid_set=set()
def antenas_type_check(grid,anten_set): # checks for full list of types of antena (characters  we have on the map ) and their position
  for row in grid:
      for element in row:
          if element != '.':
            anten_set.add(element)

  return anten_set

def antenas_position_check(anten_type,grid,anten_dict):
    for row in grid:
        for element in row:
            if element == anten_type:
                anten_position=(grid.index(row), row.index(element)) # tuple postion (row, column)
                if anten_type not in anten_dict:
                    anten_dict[anten_type]=[]
                anten_dict[element].append(anten_position)
    return anten_dict




antenas_type_check(grid,anten_set)
print(len(anten_set))
for anten_type in anten_set:
    antenas_position_check(anten_type, grid, anten_dict)
print(anten_dict)

for values in anten_dict.values():
        for i in range(len(values)):
            for j in range(i+1,len(values)):
                x1,y1=values[i]
                x2,y2=values[j]
                x_dist=abs(x2-x1)
                y_dist=abs(y2-y1)

                if x_dist == 2 * y_dist or y_dist == 2* x_dist:
                    antinodes_1=(abs(x1-(x2-x1)),abs(y1-(y2-y1)))
                    antinodes_2=(abs(x2+(x2-x1)),abs(y2+(y2-y1)))
                    antinodes_set.add(antinodes_1)
                    antinodes_set.add(antinodes_2)
                    antinodes_lst.append(antinodes_1)
                    antinodes_lst.append(antinodes_2)

print(antinodes_set)
print(antinodes_lst) # jus added list to see difference in the element lst vs set but suprisingly no difference :(
for item in antinodes_set:
    a,b= item
    if 0<=a < len(grid) and 0<=b < len(grid[0]):
        antinodes_ingrid_set.add(item)


print(antinodes_ingrid_set)
print(len(antinodes_ingrid_set))
