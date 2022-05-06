import PySimpleGUI as sg


form=sg.FlexForm("csv-to-gloss")
layout= [[sg.Text("Select the data in the following")], [sg.Text('Example file', size=(15,1)), sg.Text('Transliteration Key', size=(15,1)), sg.Text('Tex File', size=(15,1))], [sg.Submit(), sg.Cancel()]]

button, values=form.LayoutAndRead(layout)
print(button, values[0], values[1], values[2])