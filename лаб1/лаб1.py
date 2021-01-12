import pandas as pd
import numpy as np
df = pd.read_csv('lab1.csv')
columns = list(df)

print('Критерій Вальда:')
vald = []
for i in columns:
    vald.append(df[i].min())
print(vald)
vald = np.array(vald)
print('Найкращим є: ',np.argmax(vald) + 1)

print('Максимальний:')
max_ = []
for i in columns:
    max_.append(df[i].max())
print(max_)
max_ = np.array(max_)
print('Найкращим є: ',np.argmax(max_) + 1)

print('Гурвіца:')
a = 0.5
gur = {}
for i in columns:
    gur[i] = max(df[i])*0.5+min(df[i])*(1-a)
gur = list(gur.values())
print(gur)
gur = np.array(gur)
print('Найкращим є: ',np.argmax(gur) + 1)

print('Лапласса:')
lap = {}
for i in columns:
    for j in range(len(df[i])):
        if i not in lap:
            lap[i] = 0
        lap[i] += df[i][j] / len(columns)
lap = list(lap.values())
print(lap)
lap = np.array(lap)
print('Найкращим є: ',np.argmax(lap) + 1)

print('Лапласса при p1=0.5, p2=0.35, p3=0.15:')
lap2 = {}
p = [0.5,0.35,0.15]
for i in columns:
    for j in range(len(df[i])):
        if i not in lap2:
            lap2[i] = 0
        lap2[i] += df[i][j] * p[j]
lap2 = list(lap2.values())
print(lap2)
lap2 = np.array(lap2)
print('Найкращим є: ',np.argmax(lap2) + 1)
print()

results = pd.DataFrame(list(zip(vald, max_, gur, lap, lap2)),
                       columns =['Вальда', 'Максимінний','Гурвіца','Лапласа','Лапласа 2'], index = columns)
print(results)