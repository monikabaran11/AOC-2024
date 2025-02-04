from itertools import product
list=[]

with open('AOC7.txt', 'r') as file:
    for line in file:
        row=line.strip().split(':')
        list.append(row)
print(list)
result_lst=[]
combination_lst=[]
for x,y in list:
    result_lst.append(int(x))
    combination=[int(element) for element in y.strip().split()]
    combination_lst.append(combination)

print(result_lst)
print(combination_lst)

total_calibration_lst=[]
operations=['*', '+', '||']


for index, element in enumerate(combination_lst):
    operator_combinations = product(operations, repeat=len(element)-1 )

    for ops in operator_combinations:
        eval = element[0]

        for i in range(len(ops)):
            if ops[i] == "+":
                eval = eval+ element[i+1]
            elif ops[i] == "*":
                eval= eval*element[i+1]
            elif ops[i] == '||':
                eval= int(str(eval)+str(element[i+1]))


        if eval == result_lst[index]:
            total_calibration_lst.append(result_lst[index])
            break



print(total_calibration_lst)
print(sum(total_calibration_lst))