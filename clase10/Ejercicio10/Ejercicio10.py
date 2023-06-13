from tkinter import ttk
import tkinter

windows = tkinter.Tk()

windows.title("Ejercicio 10")
windows.maxsize(width=350, height=300)
windows.configure(bg='#2e2e2e')

select = tkinter.StringVar()

title_label = tkinter.Label(windows, text= 'Cursos', foreground="#1fdf64", font=("Arial", 14, 'bold'), background='#2e2e2e')
title_label.grid(row=0, column=1, sticky=tkinter.W, ipadx= 5, ipady= 5)  

selected_option = tkinter.Label(windows, text= '', foreground="#1fdf64", font=("Arial", 12, 'bold'), background='#2e2e2e')
selected_option.grid(row=7, column=1, sticky=tkinter.W, ipadx= 5, ipady= 5) 

def getTextSelected(event):
    selected_option.config(text = event.widget.cget("value"))

s = ttk.Style()                     # Creating style element
s.configure('Wild.TRadiobutton',    # First argument is the name of style. Needs to end with: .TRadiobutton
        background='#2e2e2e',         # Setting background to our specified color above
        foreground='#f0ffff')

r1 = ttk.Radiobutton(windows, text="Python",value="Python", variable=select, style=('Wild.TRadiobutton'))   
r1.bind("<Button-1>",getTextSelected)
r1.grid(row=2, column=0,padx=10,pady=10)


r2 = ttk.Radiobutton(windows, text="JavaScript",value="JavaScript", variable=select, style=('Wild.TRadiobutton'))    
r2.bind("<Button-1>",getTextSelected)
r2.grid(row=3, column=0,padx=10,pady=10)

r3 = ttk.Radiobutton(windows, text="React",value="React", variable=select, style=('Wild.TRadiobutton'))    
r3.bind("<Button-1>",getTextSelected)
r3.grid(row=4, column=0,padx=10,pady=10)

def refresh(event):
    selected_option.config(text = '')
    select.set(0)

buttonReiniciar = ttk.Button(windows, text="Refresh")
buttonReiniciar.grid(row=8, column=1, sticky=tkinter.W, padx=15, pady=15)
buttonReiniciar.bind("<Button-1>",refresh)
ttk.Button(windows, text="Quit", command=windows.destroy).grid(column=2, row=8, padx=30)

windows.mainloop()