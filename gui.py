import sys
import tkinter as tk

from monte_carlo import mc_pipeline
from calculations import (
    recommend_start_amt, recommend_withdrawal, calculate_expected_yrs)

# -------------GUI SETTINGS FOR SCALABILITY/CUSTOMIZABILITY--------------------
WINDOW_SIZE = 500
TEXT_LOC = WINDOW_SIZE - 50
FIRST_ENTRY_Y = WINDOW_SIZE/5
ENTRY_Y_DIST = WINDOW_SIZE/20
BTN_Y_DIST = 30
ENTRY_BTN_Y_DIST = 40
BG_COLOR = 'gray'

# -----------------------------------------------------------------------------


def tk_start_amt(inflation=0.035):
    '''
    modified function from calculations.py - testing tkinter integration
    recommends starting amount given retirement portfolio/condition
    '''
    try:
        withdrawal = float(wtdraw_entry.get())
        n_yrs = float(yrs_entry.get())
        pgrowth = float(growth_entry.get())

        start = recommend_start_amt(withdrawal, n_yrs, pgrowth)
        start_lbl = tk.Label(
            root, text='Recommended starting amount: %s' % round(start, 2))
        bg.create_window(
            WINDOW_SIZE/2, TEXT_LOC, window=start_lbl)

    except ValueError:
        error_lbl = tk.Label(root, text='Missing variable')
        bg.create_window(WINDOW_SIZE/2, TEXT_LOC, window=error_lbl)

# -----------------------------------------------------------------------------


def tk_recommend_withdrawal():
    try:
        starting = float(start_entry.get())
        wtdraw = recommend_withdrawal(starting)
        wtdraw_lbl = tk.Label(root, text='Recommended annual range: %s - %s'
                              % (wtdraw[0], wtdraw[1]))
        bg.create_window(
            WINDOW_SIZE/2, TEXT_LOC, window=wtdraw_lbl)

    except ValueError:
        error_lbl = tk.Label(root, text='Missing variable')
        bg.create_window(WINDOW_SIZE/2, TEXT_LOC, window=error_lbl)

# -----------------------------------------------------------------------------


def tk_calculate_expected_yrs():
    try:
        withdrawal = float(wtdraw_entry.get())
        starting = float(start_entry.get())
        pgrowth = float(growth_entry.get())

        ret_yrs = calculate_expected_yrs(withdrawal, starting, pgrowth)
        ret_yrs_lbl = tk.Label(root, text='Recommended years in retirement: %s'
                               % round(ret_yrs, 2))
        bg.create_window(
            WINDOW_SIZE/2, TEXT_LOC, window=ret_yrs_lbl)
    except ValueError:
        error_lbl = tk.Label(root, text='Missing variable')
        bg.create_window(WINDOW_SIZE/2, TEXT_LOC, window=error_lbl)

# -----------------------------------------------------------------------------


def run_monte_carlo():
    '''returns plot comparing portfolio performance to historic data'''
    try:
        starting = float(start_entry.get())
        withdrawal = float(wtdraw_entry.get())
        n_yrs = float(yrs_entry.get())
        perc_stocks = float(perc_stocks_entry.get())
        n_simul = int(n_lifes_entry.get())

        mc_pipeline(starting, withdrawal, n_yrs, perc_stocks, n_simul)
    except ValueError:
        start_lbl = tk.Label(root, text='Missing variable')
        bg.create_window(WINDOW_SIZE/2, TEXT_LOC, window=start_lbl)

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Retirement monte carlo')
    # root.configure(background=BG_COLOR)

    bg = tk.Canvas(root, width=WINDOW_SIZE, height=WINDOW_SIZE)
    # bg.configure(background=BG_COLOR)
    bg.pack()

    start_entry = tk.Entry(root)
    start_entry.insert(0, 'Starting amount')
    bg.create_window(WINDOW_SIZE/2, FIRST_ENTRY_Y, window=start_entry)

    wtdraw_entry = tk.Entry(root)
    wtdraw_entry.insert(0, 'Annual withdrawal')
    bg.create_window(WINDOW_SIZE/2, FIRST_ENTRY_Y +
                     ENTRY_Y_DIST, window=wtdraw_entry)

    yrs_entry = tk.Entry(root)
    yrs_entry.insert(0, 'Average number years')
    bg.create_window(WINDOW_SIZE/2, FIRST_ENTRY_Y +
                     ENTRY_Y_DIST*2, window=yrs_entry)

    perc_stocks_entry = tk.Entry(root)
    perc_stocks_entry.insert(0, 'Percent stocks')
    bg.create_window(WINDOW_SIZE/2, FIRST_ENTRY_Y +
                     ENTRY_Y_DIST*3, window=perc_stocks_entry)

    growth_entry = tk.Entry(root)
    growth_entry.insert(0, 'Annual return rate')
    bg.create_window(WINDOW_SIZE/2, FIRST_ENTRY_Y +
                     ENTRY_Y_DIST*4, window=growth_entry)

    n_lifes_entry = tk.Entry(root)
    n_lifes_entry.insert(0, 'n simulations')
    bg.create_window(WINDOW_SIZE/2, FIRST_ENTRY_Y +
                     ENTRY_Y_DIST*5, window=n_lifes_entry)

    recommend_start_btn = tk.Button(text='Recommend starting amount',
                                    command=tk_start_amt, bg='pink')
    bg.create_window(WINDOW_SIZE/2, FIRST_ENTRY_Y + ENTRY_BTN_Y_DIST +
                     ENTRY_Y_DIST*5 + BTN_Y_DIST, window=recommend_start_btn)

    recommend_wtd_btn = tk.Button(text='Recommend annual withdrawal',
                                  command=tk_recommend_withdrawal, bg='pink')
    bg.create_window(WINDOW_SIZE/2, FIRST_ENTRY_Y + ENTRY_BTN_Y_DIST +
                     ENTRY_Y_DIST*5 + BTN_Y_DIST*2, window=recommend_wtd_btn)

    recommend_yrs_btn = tk.Button(text='Recommended years in retirement',
                                  command=tk_calculate_expected_yrs, bg='pink')
    bg.create_window(WINDOW_SIZE/2, FIRST_ENTRY_Y + ENTRY_BTN_Y_DIST +
                     ENTRY_Y_DIST*5 + BTN_Y_DIST*3, window=recommend_yrs_btn)

    plot_btn = tk.Button(text='Generate monte-carlo plot',
                         command=run_monte_carlo, bg='pink')
    bg.create_window(WINDOW_SIZE/2, FIRST_ENTRY_Y + ENTRY_BTN_Y_DIST +
                     ENTRY_Y_DIST*5 + BTN_Y_DIST*4, window=plot_btn)
    root.mainloop()

# -----------------------------------------------------------------------------
