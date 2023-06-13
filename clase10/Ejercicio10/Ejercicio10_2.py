from tkinter import ttk
import tkinter

windows = tkinter.Tk()

windows.title("Ejercicio 10.2")
windows.columnconfigure(0, weight=1)
windows.minsize(width=350, height=300)
windows.maxsize(width=350, height=300)
windows.configure(bg='#2e2e2e')

title = tkinter.Label(windows, text= 'Lista de Lenguajes', foreground="#1fdf64", background="#2e2e2e", font=("Arial", 14))
title.grid(row=0, column=0, sticky=tkinter.W, ipadx= 5, ipady= 5) 

courses_list = ['Python', 'Java', 'C++', 'C#', 'JavaScript', 'PHP', 'Ruby', 'Swift', 'Kotlin', 'Go', 'Dart']

listBox  = tkinter.Listbox(windows, height = 20, listvariable= tkinter.StringVar(value = courses_list), foreground='#f0ffff', background='#2e2e2e', font=('Arial', 12))
listBox.grid(row=1,column=0,sticky=tkinter.S, ipadx=15, ipady=15) 


windows.mainloop()