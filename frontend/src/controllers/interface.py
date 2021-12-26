from random import randint
import PySimpleGUI as sg
from frontend.src.bin.theme import Theme
from backend.src.controllers.sorted import Start

class StartInterface:

    def __init__(self):

        Theme.themeLayout()

    def interface(self):

        buttonsRedirect = [
            [sg.B('Dado Seis Lados', key='btn_seislados')],
            [sg.B('Dado Dezeseis Lados', key='btn_dezeseislados')],
        ]

        layout = [
            [sg.Column(buttonsRedirect, justification='center')],
            [sg.B('Exit', key='btn_exit')],
        ]

        window = sg.Window('Dados',
                        layout,
                        size=(535, 550),
                        element_justification='center')

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'btn_exit':
                break
            
            if event == 'btn_seislados':
                window.close()
                from frontend.src.controllers.interfaceSeisLados import StartInterfaceSeisLados 
                Start = StartInterfaceSeisLados()
                Start.interfaceSeislados()
            
            if event == 'btn_dezeseislados':
                window.close()
                from frontend.src.controllers.interfaceDezeseisLados import StartInterfaceDezeseisLados 
                Start = StartInterfaceDezeseisLados()
                Start.interfaceDezeseisLados()


