from random import randint
from backend.src.controllers.sorted import Start
from frontend.src.bin.theme import Theme
import PySimpleGUI as sg

class StartInterfaceSeisLados:

    def __init__(self):

        Theme.themeLayout()

    def interfaceSeislados(self):

        layout = [
            [sg.Image(filename=f'{Start.dadosSeisLados(self)}')],
            [sg.B('Refresh'), sg.B('Return')],
        ]

        window = sg.Window('Dados',
                        layout,
                        size=(535, 550),
                        element_justification='center')

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == 'Refresh':
                window.close()
                self.interfaceSeislados()

            if event == 'Return':
                window.close()
                from frontend.src.controllers.interface import StartInterface
                start = StartInterface()
                start.interface()


