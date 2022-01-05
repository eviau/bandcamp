# faire un programme qui prend une liste de données financières, et la traite de la façon suivante:
# 1 - obtenir les rendements (différence en pourcentages entre deux résultats quotidiens)
# 2 - assigner une note à chaque rendement
# 3 - pour chaque note assignée, composer la str qui sera shippée à csound

import pandas

# read_csv
data = pandas.read_csv('data.csv')
print(data.head())


# assigner une note
# pour chaque note assignée, composer la str qui sera shippée à csound
start_time = 0.0
print("start of data sonification!")
for index, row in data.iterrows():
    duration = row['High'] + row['Low'] + row['Close'] + 5.0
    pp = 'i1  ' + str(start_time) + '   ' + str(duration) + '    ' + \
        str(row['High']) + \
        '     ' + str(row['Low']) + \
                '     ' + str(row['Close'])
     #   '     ' + str(row['Close']) + \

    print(pp)
    start_time=start_time + duration
