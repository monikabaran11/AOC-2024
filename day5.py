
list_of_pairs = []
with open('AOC5pairs.txt', 'r') as file:
    for line in file:
        pair = [int(x) for x in line.strip().split('|')]
        list_of_pairs.append(pair)

print(list_of_pairs)
list_of_codes=[]
with open('AOC5codes.txt', 'r') as file:
    for line in file:
        code = [int(x) for x in line.strip().split(',')]
        list_of_codes.append(code)

print(list_of_codes)

# function that check if pairs are in the list and in the right oder
lst=[57,47,82,32,18]
def order_check(lst):
    for x,y in list_of_pairs:
        if x in lst and y in lst:
            if lst.index(x) > lst.index(y):
                return 0
    return 1

print(order_check(lst))
correct_codes=[]

for lst in list_of_codes:
    if order_check(lst) == 1:
        correct_codes.append(lst)

print(correct_codes)
list_of_middle_elements=[]
for lst in correct_codes:
    middle=lst[len(lst)// 2]
    list_of_middle_elements.append(middle)
print(list_of_middle_elements)
print(sum(list_of_middle_elements))

    #srodkowy_element = lista[len(lista) // 2]