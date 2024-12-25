import re


with open('AOC3.txt', 'r') as file:
    text = file.read()


# to delete expression from don't to do all replace with ""
text_modified=re.sub(r"don't\(\).*?do\(\)",'',text,flags=re.DOTALL)
print(text_modified)
#finding expression
mul_lst=re.findall(r'mul\((\d{1,3},\d{1,3})\)',text_modified)


# modifying to integers to calc sum.
mul_numbers_lst =[i.strip().split(',') for i in mul_lst]
mul_numbers_lst=[[int(x) for x in sublist]for sublist in mul_numbers_lst]
multiply_lst=[]
for sublist in mul_numbers_lst:
    multiply=sublist[0]*sublist[1]
    multiply_lst.append(multiply)
print(multiply_lst)
print(sum(multiply_lst))