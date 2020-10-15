import PySimpleGUI as sg
import re
f = open("output.txt", "w")
layout = [[sg.Text('Enter the phrases you want to remove the capital from:')],
                 [sg.InputText()],
                 [sg.Submit(), sg.Cancel()]]

window = sg.Window('Script LowerCase', layout)

event, values = window.read()
window.close()
text_input = values[0].strip()
for a in text_input.split(' '):
    if(len(re.findall(r'[A-Z]', a[0]))):
        print(a)
        f.write(a + '\n')
sg.popup('Phrases with capital letters ignored:', a)
f.close()