import PySimpleGUI as sg

def build():
    layout=[
        [sg.Text('Las 20 consolas mas vendidas de la historia')],
        [sg.Output(key='-output-')],
        [sg.Button('hola', key='hola')]
    ]

    board = sg.Window('hola',layout=layout)
    return board

def loop():
    window = build()
    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'hola':
            break

loop()