from tkinter import *
from tkinter import ttk
from math import *


root = Tk()
root.title('Simple Calculator')

entry_display = Entry(root, text = '')
entry_display.grid(row = 0, column = 1, columnspan = 2)

def insert_number(number):
	entry_display.insert(20, number)

def execute_operation(calculated):
	entry_display.delete(0, 'end')
	entry_display.insert(2, calculated)

no7 = ttk.Button(root, text = '7', command = lambda : insert_number('7')).grid(row = 1, column = 1)
no8 = ttk.Button(root, text = '8', command = lambda : insert_number('8')).grid(row = 1, column = 2)
no9 = ttk.Button(root, text = '9', command = lambda : insert_number('9')).grid(row = 1, column = 3)
no3 = ttk.Button(root, text = '3', command = lambda : insert_number('3')).grid(row = 3, column = 3)
no4 = ttk.Button(root, text = '4', command = lambda : insert_number('4')).grid(row = 2, column = 1)
no5 = ttk.Button(root, text = '5', command = lambda : insert_number('5')).grid(row = 2, column = 2)
no6 = ttk.Button(root, text = '6', command = lambda : insert_number('6')).grid(row = 2, column = 3)
no1 = ttk.Button(root, text = '1', command = lambda : insert_number('1')).grid(row = 3, column = 1)
no2 = ttk.Button(root, text = '2', command = lambda : insert_number('2')).grid(row = 3, column = 2)
no0 = ttk.Button(root, text = '0', command = lambda : insert_number('0')).grid(row = 4, column = 2)
no_minus = ttk.Button(root, text = '-', command = lambda : insert_number('-')).grid(row = 1, column = 4)
no_plus = ttk.Button(root, text = '+', command = lambda : insert_number('+')).grid(row = 3, column = 4)
no_div = ttk.Button(root, text = '/', command = lambda : insert_number('/')).grid(row = 4, column = 1)
no_mul = ttk.Button(root, text = '*', command = lambda : insert_number('*')).grid(row = 2, column = 4)
no_zero = ttk.Button(root, text = 'AC', command = lambda : entry_display.delete(0, 'end'))
no_zero.grid(row = 4, column = 3)
no_equal = ttk.Button(root, text = '=', command = lambda : execute_operation(((float))(eval(entry_display.get())))).grid(row = 4, column = 4)


root.mainloop()