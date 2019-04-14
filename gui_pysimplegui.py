import PySimpleGUI as sg

from calculations import recommend_start_amt, recommend_withdrawal
from monte_carlo import mc_pipeline

# -------------------------------SETUP-----------------------------------------

SIZE = (30, 1)

layout = [
    [sg.Text('Portfolio information: '), sg.Text(
        '', size=(70, 1), key='_OUTPUT_')],
    [sg.Text('Starting amount', size=SIZE), sg.InputText()],
    [sg.Text('Annual withdrawal amount', size=SIZE), sg.InputText()],
    [sg.Text('Number years in retirement', size=SIZE), sg.InputText()],
    [sg.Text('Percent stocks (decimal)', size=SIZE), sg.InputText()],
    [sg.Text('Annual percent growth (decimal)', size=SIZE), sg.InputText()],
    [sg.Text('Number simulations', size=SIZE), sg.InputText()],
    [sg.Button('Starting amount'), sg.Button('Annual withdrawal'),
     sg.Button('Monte Carlo'), sg.Button('Exit')]
]

window = sg.Window('Retirement monte carlo').Layout(layout)

# -----------------------------MAIN LOOP---------------------------------------

while True:
    event, values_dict = window.Read()
    values = list(values_dict.values())
    try:
        values = [float(x) for x in values]
        values[2] = int(values[2])  # n_yrs as int
        values[5] = int(values[5])  # n_iter as int
    except TypeError:
        # if missing a value, though usually fine since most calculations
        # dont require all values
        pass

    if event == 'Starting amount':
        start = recommend_start_amt(values[1], values[2], values[4])
        window.FindElement('_OUTPUT_').Update(
            'Recommended starting amount: %s' % start)
    if event == 'Annual withdrawal':
        low, high = recommend_withdrawal(values[0])
        window.FindElement('_OUTPUT_').Update(
            'Recommended annual withdrawal range: %s - %s' % (low, high))
    if event == 'Monte Carlo':
        mc_pipeline(values[0], values[1], values[2], values[3], values[5])
    if event == 'Exit':
        break

window.Close()
