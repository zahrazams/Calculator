from tkinter import *

wn = Tk()

wn.geometry("400x400")

wn.title("Calculator")

def add():
    first_number = no1_entry_data.get()
    second_number = no2_entry_data.get()
    result_lbl.config(text= int(first_number) + int(second_number))

def sub():
    first_number = no1_entry_data.get()
    second_number = no2_entry_data.get()
    result_lbl.config(text= int(first_number) - int(second_number))

def mult():
    first_number = no1_entry_data.get()
    second_number = no2_entry_data.get()
    result_lbl.config(text= int(first_number) * int(second_number))

def div():
    first_number = no1_entry_data.get()
    second_number = no2_entry_data.get()
    result_lbl.config(text= int(first_number) / int(second_number))

def clear():
    no1_entry_data.delete(0,END)
    no2_entry_data.delete(0,END)
    result_lbl.config(text= "Result")

title_lbl = Label(text = "Calculator", font = ("Georgia",25,"bold"))
no1_lbl = Label(text = "First Number", font = ("Cambria",15))
no1_entry_data = Entry(wn)
no2_lbl = Label(text = "Second Number", font = ("Cambria",15))
no2_entry_data = Entry(wn)
result_lbl = Label(text = "Result", font = ("Cambria",15))
btn2_click = Button(wn, text = "+", width = 20, height = 1, command=add)
btn3_click = Button(wn, text = "-", width = 20, height = 1, command=sub)
btn4_click = Button(wn, text = "x", width = 20, height = 1, command=mult)
btn5_click = Button(wn, text = "/", width = 20, height = 1, command=div)
btn6_click = Button(wn, text = "Clear", width = 20, height = 1, command=clear)

title_lbl.pack()
no1_lbl.pack()
no1_entry_data.pack()
no2_lbl.pack()
no2_entry_data.pack()
result_lbl.pack()
btn2_click.pack()
btn3_click.pack()
btn4_click.pack()
btn5_click.pack()
btn6_click.pack()
