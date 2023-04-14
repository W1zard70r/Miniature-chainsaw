\import PySimpleGUI as sg


sg.theme('LightBlue2')  # Set the theme

s=['1','2','3']
a=[
'''
for i in range():
    print('')''',
'''
for x in range():
    print('')''',
'''
for z in range():
    print('')'''
]
# Define the layout
layout = [[sg.Text('Input Text:', font=('Arial', 12)), sg.InputText(key='input')],
         [sg.Text('Input number of text:', font=('Arial', 12)), sg.InputText(key='inputt')],
          [sg.Text('added:', font=('Arial', 12)), sg.Text('', size=(40, 1), key='output')],
          [sg.Combo(s, default_value=s[0], s=(15,22), enable_events=True, readonly=True, k='-COMBO-', key='Combo'),
          sg.Output(s=(40,10), key='outputt')],
          [sg.Button('Process Input', font=('Arial', 12), button_color=('white', '#4CAF50'), key='process'),
           sg.Button('Someth', font=('Arial', 12), button_color=('white', '#4CAF50'), key='button'),sg.Button('to add', font=('Arial', 12), button_color=('white', '#4CAD50'), key='buttonn')]]

# Create the window
window = sg.Window('ЕГЭ by Alexandr Silkov', layout)

# Event loop
while True:
    event, values = window.read()

    # Exit the app when the window is closed
    if event == sg.WINDOW_CLOSED:
        break

    # Process the input and update the output when the button is clicked
    if event == 'buttonn':
        input_text = values['input']
        input_num= values['inputt']
        a.append(input_text)
        s.append(str(input_num))
        window['output'].update('')
    if event == 'process':
        input_text = values['input']
        input_num= values['inputt']
        window['outputt'].update('')
        choice=a[int(values['Combo'])-1]
        window['input'].update('')
        window['output'].update(input_text)
        print(s)
        print(a)
    if event == 'button':
        break
