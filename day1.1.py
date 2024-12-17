import pandas as pd
# saving data as txt
df = pd.read_csv('AOCinput_day_1.txt', sep='   ', engine='python', header=None)
# data frame with to columns
df.columns = ['List1','List2']

df['List1'] = df['List1'].astype(int).sort_values().values
df['List2'] = df['List2'].astype(int).sort_values().values
# creating column as abs difference between elements on List1 and 2
df['List3'] = (df['List1']-df['List2']).abs()

result = sum(df['List3'])
print(df)
print(result)

#1.2 day one extension
#creating set with common elements of this two lists.
common_elements = set(df['List1']) & set(df['List2'])
# checking if first list/column have any duplicates
numbers1 = df['List1'].value_counts(ascending=True)
print(numbers1)
#checking if second list have duplicates and creating the df with the values od duplicate as column.
numbers2= df['List2'].value_counts(ascending=True).reset_index()
numbers2.columns = ['Value', 'Count']
numbers2['Count']=numbers2['Count'].astype(int)
print(numbers2)
#checking if common elements in number2 df and adding to dictionary where key is number and value it count.
common_with_counts={}
for number in common_elements:
    if number in numbers2['Value'].values:
        count=int(numbers2.loc[numbers2['Value'] ==number,'Count'].values[0])
        common_with_counts[number] = count
print(common_with_counts)
# cal similarity score
similarity_calc=[]
for number,count in common_with_counts.items():
    similarity_calc.append(number*count)
print(similarity_calc)
similatiry_score = sum(similarity_calc)
print(similatiry_score)
