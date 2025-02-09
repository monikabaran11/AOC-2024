

with open('AOC9a.txt', 'r') as file:
        disk_map_str=" ".join(line.strip() for line in file)



print(len(disk_map_str))

files_lst=[]
free_space_lst=[]
individual_blocks_file=[]
individual_blocks_space=[]
individual_blocks_all=[]
individual_blocks_str=""


for index, item in enumerate(disk_map_str):
    if index % 2==0: #all index even items will be files
        files_lst.append(int(item))


    elif index %2  !=0: #all index odd items will be free space
        free_space_lst.append(int(item))


#print(files_lst)
#print(free_space_lst)
for index, x in enumerate(files_lst):
    individual_blocks_file.append(str(index) * x)

for index, y in enumerate(free_space_lst):
    individual_blocks_space.append("." * y )

#print(individual_blocks_file)
#print(individual_blocks_space)


for i in range(len(individual_blocks_file)): # using len for this one as this is longer by one than the other. List will have all the agregated(multiply)items as its elements.
    individual_blocks_all.append(individual_blocks_file[i])
    if i<len(individual_blocks_space):
        individual_blocks_all.append(individual_blocks_space[i])
#print(individual_blocks_all)

individual_blocks_str="".join(individual_blocks_all) #join all toherther to then split it onr by one as list for futher operations.
#print(individual_blocks_str)
individual_blocks_lst=list(individual_blocks_str)
#print(individual_blocks_lst)
for i in range(len(individual_blocks_lst)):# here we search for '.' and mowve the first number form the left for its place.
     if individual_blocks_lst[i]=='.':
         r_i=(len(individual_blocks_lst)-1)
         while individual_blocks_lst[r_i] == '.':
             r_i-=1
             if r_i<= i:
                 break
         individual_blocks_lst[i],individual_blocks_lst[r_i]=individual_blocks_lst[r_i],individual_blocks_lst[i]

     #print(individual_blocks_lst)

print(individual_blocks_lst)
file_compacting_str=''.join(individual_blocks_lst) #converting to string only to control output.
print(file_compacting_str)

filesystem_checksum_lst=[] # list with the inx * element calc.
for index, item in enumerate(individual_blocks_lst):
    if item != '.':
        fileID=(index*int(item))
        filesystem_checksum_lst.append(fileID)

print(sum(filesystem_checksum_lst)) #final result.