import tkinter as tk

from monte_carlo import mc_pipeline

# -------------GUI SETTINGS FOR SCALABILITY/CUSTOMIZABILITY--------------------
WINDOW_SIZE = 500
TEXT_LOC = WINDOW_SIZE - 125
FIRST_ENTRY_Y = WINDOW_SIZE/5
ENTRY_Y_DIST = WINDOW_SIZE/20
BTN_Y_DIST = 50
BG_COLOR = 'gray'

# -----------------------------------------------------------------------------


def recommend_start_amt(inflation=0.035):
    '''
    modified function from calculations.py - testing tkinter integration
    recommends starting amount given retirement portfolio/condition
    '''
    try:
        withdrawal = float(wtdraw_entry.get())
        n_yrs = float(yrs_entry.get())
        pgrowth = float(growth_entry.get())

        start = withdrawal/((pgrowth-inflation) *
                            (1 - pow((1+inflation)/(1+pgrowth), n_yrs)))
        start_lbl = tk.Label(
            root, text='Recommended starting amount: %s' % round(start, 2))
        bg.create_window(
            WINDOW_SIZE/2, 230, window=start_lbl)

    except ValueError:
        start_lbl = tk.Label(root, text='Missing variable')
        bg.create_window(WINDOW_SIZE/2, TEXT_LOC, window=start_lbl)

# -----------------------------------------------------------------------------


def recommend_withdrawal():
    pass

# -----------------------------------------------------------------------------


def calculations_expected_yrs():
    pass

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
                                    command=recommend_start_amt, bg='pink')
    bg.create_window(WINDOW_SIZE/2, FIRST_ENTRY_Y +
                     ENTRY_Y_DIST*5 + BTN_Y_DIST, window=recommend_start_btn)

    plot_btn = tk.Button(text='Generate monte-carlo plot',
                         command=run_monte_carlo, bg='pink')
    bg.create_window(WINDOW_SIZE/2, FIRST_ENTRY_Y +
                     ENTRY_Y_DIST*5 + BTN_Y_DIST*2, window=plot_btn)
    root.mainloop()

# -----------------------------------------------------------------------------
