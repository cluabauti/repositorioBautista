from src.windows import menu as menu_ventana
from src.handlers import menu as menu_handler
import PySimpleGUI as sg

def start ():
    '''
    Lanza la ejecucion del menu
    '''
    window = loop()
    window.close()



def loop():
    '''
    Loop de la ventana del menu que capta los eventos
    '''
    window = menu_ventana.build()
    while True:
        event, _values = window.read()

        if event == "exit":
            break
        if event == "-arboles-":
            window.hide()
            menu_handler.start('-arboles-')
            window.un_hide()

        if event == "-consolas-":
            window.hide()
            menu_handler.start('-consolas-')
            window.un_hide()
    return window