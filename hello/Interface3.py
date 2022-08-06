from tkinter import *

quincena = 0
ahorroUno = 0
ahorroDos = 0
ahorroTres = 0
ahorroCuatro = 0

ahorroTotal = 0
ahorroMensual = 0

salario = 2000

ahorroUno = salario * 40 / 100
ahorroDos = salario * 30 / 100
ahorroTres = salario * 20 / 100
ahorroCuatro = salario * 10 / 100

master = Tk()
Label(master, text='Ahorro 40% Pagos fijos').grid(row=0)
Label(master, text='Ahorro 30% transporte').grid(row=1)
Label(master, text='Ahorro 20% Comida').grid(row=2)
Label(master, text='Ahorro 10% Para lo que sea').grid(row=3)
button = Button(master, text='Stop', width=25, command=master.destroy).grid(row=4)
Label(master, text=ahorroUno).grid(row=0, column=1)
Label(master, text=ahorroDos).grid(row=1, column=1)
Label(master, text=ahorroTres).grid(row=2, column=1)
Label(master, text=ahorroCuatro).grid(row=3, column=1)




mainloop()