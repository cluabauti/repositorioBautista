import PySimpleGUI as sg
def build():
    '''
    Construye la ventana del menu
    '''
    layout = [
        [sg.Text("Actividad 1 x Python Plus - TEORIA -",font=('Roboto', 14), justification='center', text_color='pink', background_color = 'black')],
        [sg.Text("¿Qué datos analizamos?",font=('Currier new', 14), justification='center', text_color='red', background_color = 'white')],
        [sg.Button('Especies de arboles en LP', size=(70,3), key="-arboles-")],
        [sg.Button('Consolas de videojuegos', size=(70,3), key="-consolas-")],
        [sg.Button('Salir',size=(70,3), key="exit")]
    ]

    board = sg.Window("Actividad 1 x Python Plus - TEORIA -", layout=layout, no_titlebar=True,margins=(20,20))
    return board