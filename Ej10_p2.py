valores_scrabble = {1: ['A','E','I','O','U','L','N','R','S','T'], 
2: ['D','G'], 
3:['B', 'C', 'M', 'P'],
4: ['F', 'H', 'V', 'W', 'Y'],
5: 'K',
8: ['J','X'],
10: ['Q','Z']}

puntos = (1, 2, 3, 4, 5, 8, 10)
def verificar_valor (letra : str):
    '''Recibe una letra y devuelve el puntaje de la letra'''
    i = 0
    pts = 0
    encontre = False
    while not encontre:
        if  letra in valores_scrabble[puntos[i]]:
            pts = puntos[i]
            encontre = True
        else:
            i += 1
    return pts
                
    

palabra = input('Ingrese una palabra (\'FIN\' para terminar): ').upper()
pts = 0
while (palabra != 'FIN'):
    for letra in palabra:
        pts += verificar_valor(letra)
    print(f'{palabra.capitalize()}: {pts} puntos.')
    palabra = input('Ingrese una palabra (\'FIN\' para terminar): ').upper()
    pts = 0