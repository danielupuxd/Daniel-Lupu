import PySimpleGUI as sg
import random

sg.theme('LightBlue')

# Am definit interfata folosing sg  buton pentru butonul de generare aleatoriu, sg radio a fost folosit pentru a putea face variantele
layout = [
    [sg.Button('Generează Număr Aleatoriu', key='-GENEREAZA-', border_width=2)],
    [sg.Text('', size=(20, 2), key='-OUTPUT-', font=('Helvetica', 15))],
    [sg.Radio("Ana", "Fete", key="-Ana-"), 
     sg.Radio("Elena", "Fete", key="-Elena-"), 
     sg.Radio("Larisa", "Fete", key="-Larisa-")],
    [sg.Radio("Portocale", "FRUCTE", key="-PORTOCALE-", background_color="orange"), 
     sg.Radio("Mere", "FRUCTE", key="-MERE-", background_color="red"), 
     sg.Radio("Pere", "FRUCTE", key="-PERE-", background_color="green")],
]

# Dimensiunea ferestrelor
window_size = (300, 150)
window = sg.Window('Generator Număr Aleatoriu', layout, size=window_size)

# Am creat un loop pentru fereastra mea
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    # am scris evenimentele din interfata, pentru a le selecta
    selected_name = None
    selected_color = None

    if values["-Ana-"]:
        selected_name = "Ana"
    elif values["-Elena-"]:
        selected_name = "Elena"
    elif values["-Larisa-"]:
        selected_name = "Larisa"

    # variantele de ales penntru a putea face actiuneaea dorite fereastra
    selected_fruit = None
    if values["-PORTOCALE-"]:
        selected_fruit = "Portocale"
        selected_color = "orange"
    elif values["-MERE-"]:
        selected_fruit = "Mere"
        selected_color = "red"
    elif values["-PERE-"]:
        selected_fruit = "Pere"
        selected_color = "green"

    # am scris valoarea ce vreau sa fiu geneerata si ceea ce vreau sa imi afiseze dupa apasarea butonului
        #Genereaza Numar Aleatoriu
    if event == '-GENEREAZA-':
        numar_aleatoriu = random.randint(1, 100)
        window['-OUTPUT-'].update(f'{selected_name} are {numar_aleatoriu} de {selected_fruit.lower()} de culoare {selected_color}')

# Închide fereastra la final
window.close()