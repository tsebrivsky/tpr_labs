import operator
import pandas as pd
header_list = ['count', 'candidat1', 'candidat2', 'candidat3']
df = pd.read_csv('data.csv', names=header_list)

sum_ = df['count'].sum()
A, B, C, AB, BA, AC, CA, CB, BC = 0, 0, 0, 0, 0, 0, 0, 0, 0
AB = df[(df.candidat1 == 'A')|((df.candidat2 == 'A' )&(df.candidat3 == 'B'))]['count'].sum()
BA = sum_ - AB
AC = df[(df.candidat1 == 'A')|((df.candidat2 == 'A' )&(df.candidat3 == 'C'))]['count'].sum()
CA = sum_ - AC
BC = df[(df.candidat1 == 'B')|((df.candidat2 == 'B' )&(df.candidat3 == 'C'))]['count'].sum()
CB = sum_ - BC

dic = {'А більше Б':[AB],'А більше С':[AC],'Б більше А':[BA],'Б білше С':[BC],'С більше А':[CA],'С більше Б':[CB],}
result = pd.DataFrame(dic)
print('Метод Кондорсе:')
print(result)

if AB>BA and AC>CA:
    print('Виграє кандидат А')
elif BA>AB and BC>CB:
    print('Виграє кандидат Б')
elif CA>AC and CB>BC:
    print('Виграє кандидат С')
else:
    print('Переможця немає')
print()
# Метод Борда
def bord(row, candidat):
    sum_ = 0
    if row.candidat1 == candidat:
        sum_ += int(row['count'])*3
    elif row.candidat2 == candidat:
        sum_ += int(row['count'])*2
    elif row.candidat3 == candidat:
        sum_ += int(row['count'])*1
    return sum_


A = df.apply(bord,candidat = 'A', axis = 1).sum()
B = df.apply(bord,candidat = 'B', axis = 1).sum()
C = df.apply(bord,candidat = 'C', axis = 1).sum()
dic2 = {'Кандидат А':[A],'Кандидат Б':[B],'Кандидат С':[C],}
result2 = pd.DataFrame(dic2)
print('Метод Борда:')
print(result2)
print('Виграє:',max(dic2.items(), key=operator.itemgetter(1))[0])