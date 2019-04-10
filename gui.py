import tkinter as tk

root = tk.Tk()

bg = tk.Canvas(root, width=400, height=300)
bg.pack()

'''
experimental section on setting up entry text
wtdraw = tk.StringVar()
wtdraw.set('withdrawal: ')
wtDir = tk.Label(root, textvariable=wtdraw, height=4)
wtDir.pack(side='left')

directory = tk.StringVar(None)
dirname = tk.Entry(root, textvariable=directory, width=50)
dirname.pack(side="left")
'''

wtdraw_entry = tk.Entry(root)
bg.create_window(200, 100, window=wtdraw_entry)
wtd = wtdraw_entry.get()

yrs_entry = tk.Entry(root)
bg.create_window(200, 125, window=yrs_entry)
#yrs = yrs_entry.get()

growth_entry = tk.Entry(root)
bg.create_window(200, 150, window=growth_entry)
#growth = growth_entry.get()


def recommend_start_amt(inflation=0.035):
    '''
    modified function from calculations.py - testing tkinter integration
    recommends starting amount given retirement portfolio/condition
    '''
    withdrawal = float(wtdraw_entry.get())
    n_yrs = float(yrs_entry.get())
    pgrowth = float(growth_entry.get())

    start = withdrawal/((pgrowth-inflation) *
                        (1 - pow((1+inflation)/(1+pgrowth), n_yrs)))
    start_lbl = tk.Label(root, text=round(start, 2))
    bg.create_window(200, 230, window=start_lbl)


recommend_start_btn = tk.Button(
    text='Recommend starting amount', command=recommend_start_amt, bg='pink')
bg.create_window(200, 180, window=recommend_start_btn)

root.mainloop()
