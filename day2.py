list_of_reports=[]

with open('AOCday2.txt', 'r') as file:

    for line in file:
        clean_line=[int(x) for x in line.strip().split()]
        list_of_reports.append(clean_line)

print(list_of_reports)
#lst=[1, 2, 1, 7, 9, 8]
def difference_check(lst):
    result=[]
    for i in range (len(lst)-1):
        if lst[i+1]-lst[i]>=1 and lst[i+1]-lst[i]<=3:
            result.append(2)
        elif lst[i]-lst[i+1]>=1 and lst[i]-lst[i+1]<=3:
            result.append(1)
        else:
            result.append(0)
    if all(num==1 for num in result) or all(num==2 for num in result):
        return 1
    else:

        return 0

check_of_reports=[]

for lst in list_of_reports:
    check_of_reports.append(difference_check(lst))
    x=0
    lst_mod=[]
    while difference_check(lst) == 0 and x<=(len(lst)):
        lst_mod = lst[:x] + lst[x + 1:]
        if difference_check(lst_mod)==1:
            check_of_reports.append(difference_check(lst_mod))
            break
        else:
            x=x+1

print(sum(check_of_reports))





#for lst in list_of_reports

