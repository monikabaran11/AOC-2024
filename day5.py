
list_of_pairs = []
with open('AOC5pairs.txt', 'r') as file:
    for line in file:
        pair = [int(x) for x in line.strip().split('|')]
        list_of_pairs.append(pair)

print(list_of_pairs)

list_of_pairs_sorted = sorted(list_of_pairs,key=lambda x: x[0])
print(list_of_pairs_sorted)
list_of_codes=[]
with open('AOC5codes.txt', 'r') as file:
    for line in file:
        code = [int(x) for x in line.strip().split(',')]
        list_of_codes.append(code)

print(list_of_codes)

# function that check if pairs are in the list and in the right oder

def order_check(lst):
    for x,y in list_of_pairs:
        if x in lst and y in lst:
            if lst.index(x) > lst.index(y):
                return 0
    return 1

# function that fix the incorrect order.# for part 2

def order_fix(lst): # for part 2
    for x, y in list_of_pairs_sorted:
        if x in lst and y in lst:
            if lst.index(x) > lst.index(y):
                lst.remove(x)
                lst.insert(lst.index(y),x)

    return lst


correct_codes=[]
incorrect_codes=[] # for part 2

for lst in list_of_codes:
    if order_check(lst) == 1:
        correct_codes.append(lst)
    elif order_check(lst) == 0:
        incorrect_codes.append(lst)



list_of_middle_elements=[]
for lst in correct_codes:
    middle=lst[len(lst)// 2]
    list_of_middle_elements.append(middle)
print(list_of_middle_elements)
print(sum(list_of_middle_elements))


fixed_codes=[]
list_of_middle_fixed_elements = []
for lst_incorrect in incorrect_codes:
    fixed_codes.append(order_fix(lst_incorrect))

for lst_fixed in fixed_codes:
    middle2 = lst_fixed[len(lst_fixed)// 2]
    list_of_middle_fixed_elements.append(middle2)


print(list_of_middle_fixed_elements)
print(sum(list_of_middle_fixed_elements))