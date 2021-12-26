from random import randint
from backend.src.controllers.sorted import Start
from frontend.src.bin.theme import Theme
import PySimpleGUI as sg

class StartInterfaceDezeseisLados:

    def __init__(self):

        Theme.themeLayout()

    def interfaceDezeseisLados(self):

        layout = [
            [sg.T()],
            [sg.Image(filename=f'{Start.dadosDezeseisLados(self)}')],
            [sg.T()],
            [sg.B('Refresh'), sg.B('Return')],
        ]

        window = sg.Window('Dados',
                        layout,
                        size=(400, 400),
                        element_justification='center')

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == 'Refresh':
                window.close()
                self.interfaceDezeseisLados()

            if event == 'Return':
                window.close()
                from frontend.src.controllers.interface import StartInterface
                start = StartInterface()
                start.interface()


