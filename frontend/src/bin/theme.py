import PySimpleGUI as sg

class Theme:
    
    def themeLayout():

        theme = sg.SetOptions(background_color='#363636',
                    text_element_background_color='#363636',
                    element_background_color='#363636',
                    scrollbar_color=None,
                    input_elements_background_color='#F7F3EC',
                    button_color=('white', '#4F4F4F'))
                
        return theme
