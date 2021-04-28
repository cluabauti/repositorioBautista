import csv
archivo = open("D:\Desktop\_appstore_games.csv", "r")
csvreader = csv.reader(archivo, delimiter=',')

encabezado = next(csvreader)
print (encabezado)


valores = []

for linea in csvreader:
    '''if linea[7] == '0' and 'ES' in linea[12] :
        print(linea,'\n')'''
    valores.append(linea[6])

theset = sorted(valores, reverse=True)
dicci = {}
for i in range(10):
    dicci[theset[i]] = valores.index(theset[i])

print(dicci)


archivo.close()