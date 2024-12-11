
list1 = [3,4,2,1,3,3]
list2 = [4,3,5,3,9,3]
list1.sort()
list2.sort()
print(list1)
print(list2)
list3=[]
for i in range(6):
    list3.append(abs(list1[i]- list2[i]))

print(list3)
sum=sum(list3)
print(sum)