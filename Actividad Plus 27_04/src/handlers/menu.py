import PySimpleGUI as sg
import csv
import json
import os

def start (boton):    
    current_path = os.getcwd()
    files_path = os.path.join('src','Archivos')
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
        for arbol in csvreader:
            print (arbol[0])

def data_consolas (current_path, files_path, file_name):
    with open(os.path.join(current_path, files_path, file_name), 'r') as archivo:
        csvreader = csv.reader(archivo, delimiter=',')
        encabezado = next(csvreader)        
        consolas = list(lambda cons: for cons [0] in csvreader)
        ventas = list(lambda vent : vent[4] in  csvreader)
        sorted(ventas)
        