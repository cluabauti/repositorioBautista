import PySimpleGUI as sg
import csv
import json
import os

def start (boton):    
    current_path = os.getcwd()
    files_path = os.path.join('Actividad Plus 27_04/src/Archivos')
    if boton == '-arboles-':
        file_name = 'especies-de-arboles-en-la-ciudad-de-la-plata-2.csv'
        data_arboles(current_path, files_path, file_name)
    elif boton == '-consolas-':
        file_name = 'console.csv'
        data_consolas(current_path, files_path, file_name)  

def data_arboles(current_path, files_path, file_name):    
    with open(os.path.join(current_path, files_path, file_name), 'r') as archivo:
        csvreader = csv.reader(archivo, delimiter=';')
        encabezado = next(csvreader)
        arboles = []     
        arc = open('Actividad Plus 27_04/src/Archivos/arboles.json','w', encoding='UTF-8')   
        for arbol in csvreader:
            arboles.append({'Arbol':arbol[0], 'Direccion':arbol[1]})        
        
        json.dump(arboles, arc, indent=4)
        arc.close()
        sg.popup('Se han guardado todos los arboles con sus direcciones', 'de la ciudad de La PLata')

def data_consolas (current_path, files_path, file_name):
    with open(os.path.join(current_path, files_path, file_name), 'r') as archivo:
        csvreader = csv.reader(archivo, delimiter=',')
        encabezado = next(csvreader)        
        print(encabezado)
        consolas = []
        #ya ingresan ordenadas las consolas
        for i in range(20): 
            cons = next(csvreader)
            print (cons[1], cons[4])           
            consolas.append({'Nombre': cons[1],'Ventas':cons[4]})            

    arc = open('Actividad Plus 27_04/src/Archivos/Consolas.json','w', encoding='UTF-8')
    json.dump(consolas, arc, indent=4)
    arc.close()
    sg.popup('Se han guardado las 20 consolas mas vendidas',
    'de la historia en la carpeta DataSets',title='Consolas')