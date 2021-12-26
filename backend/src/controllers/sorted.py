from random import randint
import PySimpleGUI as sg

class Start:

    def dadosSeisLados(self):

        file = f'./frontend/src/assets/seislados/dice {randint(1, 6)}.png'
        return file
    
    def dadosDezeseisLados(self):

        file = f'./frontend/src/assets/dezeseislados/{randint(1, 16)}.png'
        return file




