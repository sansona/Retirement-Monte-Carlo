import tkinter as tk

from monte_carlo import mc_pipeline
from calculations import recommend_start_amt, recommend_withdrawal

# -------------GUI SETTINGS FOR SCALABILITY/CUSTOMIZABILITY--------------------
WINDOW_SIZE = 500
TEXT_LOC = WINDOW_SIZE - 50
FIRST_ENTRY_Y = WINDOW_SIZE/5
ENTRY_Y_DIST = WINDOW_SIZE/20
BTN_Y_DIST = 30
ENTRY_BTN_Y_DIST = 40
BG_COLOR = 'gray'

# -----------------------------------------------------------------------------


def missing_val_lbl():
    '''wrapper for generating message for missing value'''
    error_lbl = tk.Label(root, text='Missing value')
    bg.create_window(WINDOW_SIZE/2, TEXT_LOC, window=error_lbl)

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
        missing_val_lbl()

# -----------------------------------------------------------------------------


def tk_recommend_withdrawal():
    '''tk integration of recommend_withdrawal()'''
    try:
        starting = float(start_entry.get())
        wtdraw = recommend_withdrawal(starting)
        wtdraw_lbl = tk.Label(root, text='Recommended annual withdrawal '
                              + 'range: %s - %s' % (wtdraw[0], wtdraw[1]))
        bg.create_window(
            WINDOW_SIZE/2, TEXT_LOC, window=wtdraw_lbl)

    except ValueError:
        missing_val_lbl()

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
        missing_val_lbl()

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    # -------------------------INITIALIZE TK-----------------------------------
    root = tk.Tk()
    root.title('Retirement monte carlo')
    bg = tk.Canvas(root, width=WINDOW_SIZE, height=WINDOW_SIZE)
    # root.configure(background=BG_COLOR)
    # bg.configure(background=BG_COLOR)
    bg.pack()

    # ---------------------------ENTRY BOXES-----------------------------------
    start_entry = tk.Entry(root)
    start_entry.insert(0, 'Starting amount')
    bg.create_window(WINDOW_SIZE/2, FIRST_ENTRY_Y, window=start_entry)

    wtdraw_entry = tk.Entry(root)
    wtdraw_entry.insert(0, 'Annual withdrawal')
    bg.create_window(WINDOW_SIZE/2, FIRST_ENTRY_Y +
                     ENTRY_Y_DIST, window=wtdraw_entry)

    yrs_entry = tk.Entry(root)
    yrs_entry.insert(0, 'Years in retirement')
    bg.create_window(WINDOW_SIZE/2, FIRST_ENTRY_Y +
                     ENTRY_Y_DIST*2, window=yrs_entry)

    perc_stocks_entry = tk.Entry(root)
    perc_stocks_entry.insert(0, 'Percent stocks (decimal)')
    bg.create_window(WINDOW_SIZE/2, FIRST_ENTRY_Y +
                     ENTRY_Y_DIST*3, window=perc_stocks_entry)

    growth_entry = tk.Entry(root)
    growth_entry.insert(0, 'Annual return rate (decimal)')
    bg.create_window(WINDOW_SIZE/2, FIRST_ENTRY_Y +
                     ENTRY_Y_DIST*4, window=growth_entry)

    n_lifes_entry = tk.Entry(root)
    n_lifes_entry.insert(0, 'n simulations')
    bg.create_window(WINDOW_SIZE/2, FIRST_ENTRY_Y +
                     ENTRY_Y_DIST*5, window=n_lifes_entry)

    # -------------------------------BUTTONS-----------------------------------

    recommend_start_btn = tk.Button(text='Recommend starting amount',
                                    command=tk_start_amt, bg='pink')
    bg.create_window(WINDOW_SIZE/2, FIRST_ENTRY_Y + ENTRY_BTN_Y_DIST +
                     ENTRY_Y_DIST*5 + BTN_Y_DIST, window=recommend_start_btn)

    recommend_wtd_btn = tk.Button(text='Recommend annual withdrawal',
                                  command=tk_recommend_withdrawal, bg='pink')
    bg.create_window(WINDOW_SIZE/2, FIRST_ENTRY_Y + ENTRY_BTN_Y_DIST +
                     ENTRY_Y_DIST*5 + BTN_Y_DIST*2, window=recommend_wtd_btn)

    plot_btn = tk.Button(text='Generate monte-carlo plot',
                         command=run_monte_carlo, bg='pink')
    bg.create_window(WINDOW_SIZE/2, FIRST_ENTRY_Y + ENTRY_BTN_Y_DIST +
                     ENTRY_Y_DIST*5 + BTN_Y_DIST*3, window=plot_btn)

    root.mainloop()

# -----------------------------------------------------------------------------
