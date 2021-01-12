import nashpy as nash
import numpy as np
import pandas as pd
df = pd.read_csv('data.csv')

def minrow(row):
    return row.min()
desc = df.describe()
new_df = df.copy()
new_df['amin'] = new_df.apply(minrow, axis=1)
new_df.loc['bmax'] = desc.loc['max']
new_df

bmax = new_df.loc['bmax'].min()
amin = new_df['amin'].max()
bmaxid = new_df.loc['bmax'].idxmin()
aminid = new_df['amin'].idxmax()
print('Сідлова точка:',new_df[bmaxid][aminid])
print(f'Стовбець: {bmaxid}, Рядок: {aminid}')

# Знаходження домінуючих рядків
print('Знаходження домінуючих рядків:')
n = df.shape[0]
adellist = set()
for i in range(n):
    for j in range(n):
        if i != j and (df.loc[i] >= df.loc[j]).sum() == 5:
            print(f'{list(df.loc[i])} домінує над ,{list(df.loc[j])}')
            adellist.add(j)
# знаходження домінуючих стовпців
print('Знаходження домінуючих стовпців:')
n = df.shape[1]
bdellist = set()
for i in df.columns:
    for j in df.columns:
        if i != j and (df[i] <= df[j]).sum() == 5:
            print(f'{list(df[i])} домінує над ,{list(df[j])}')
            bdellist.add(j)

df.drop(adellist, inplace=True)
df.drop(bdellist, axis=1, inplace=True)

df2 = df.copy()
desc2 = df2.describe()
df2['amin'] = df2.apply(minrow, axis=1)
df2.loc['bmax'] = desc2.loc['max']
print(df2)

if bmax != amin:
    print('Нижня ціна гри:',amin)
    print('Верхня ціна гри:',bmax)
    print(f'Гра не має вирішення в чистих стратегій: {bmax} != {amin}')
    arr = pd.read_csv('data.csv').to_numpy()
    print(arr)
    game = nash.Game(arr)
    list2 = list(game.vertex_enumeration())[0]
    print('Оптимальні змішані стратегії гравця А:')
    print(list2[0])
    print('Оптимальні змішані стратегії гравця B:')
    print(list2[1])
    print('Ціна гри:')
    print(game[list2[0],list2[1]][0])
else:
    print(f'Гра має вирішення в чистих стратегій, ціна гри: {bmax}')