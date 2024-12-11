import pandas as pd
# saving data as txt
df = pd.read_csv('AOCinput_day_1.txt', sep='   ', engine='python', header=None)
# data frame with to columns
df.columns = ['List1','List2']
# changing data to string, separating the numbers

df['List1'] = df['List1'].apply(lambda x: [",".join(str(x))])
df['List2'] = df['List2'].apply(lambda x: [",".join(str(x))])
#changing string to separate each element by "," and changing elements to int  and finally sorting.
df['List1'] = df['List1'].apply(lambda x: sorted([int(i) for i in x[0].split(',')]))
df['List2'] = df['List2'].apply(lambda x: sorted([int(i) for i in x[0].split(',')]))
# creating column as abs difference between elements on List1 and 2
df['List3'] = df.apply(lambda row: [abs(row['List1'][i]-row['List2'][i]) for i in range(5)],axis=1)
df['Sum'] = df.apply (lambda row: sum(row['List3']),axis=1)
print(df['Sum'].dtype)
#sum for final result
result = df['Sum'].sum()
print(df)
print(result)
totals=df.sum()
print(totals)
