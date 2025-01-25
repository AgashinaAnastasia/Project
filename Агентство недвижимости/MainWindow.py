from tkinter import *
import tkinter as tk
from Buyer import BuyerWin
from Report import ReportWin
from Task import TaskWin
import pyodbc
import pandas as pd
def Buyer():
    BuyerWin()
def Seller():
    pass

def Realty():
    pass

def Report():
    ReportWin()

def Tasks():
    TaskWin()

window1 = Tk()
window1.title('Риэлторсикй отдел')
window1.geometry('300x320')
window1.configure(bg='#5CDB95')

title = tk.Label(window1, text='Главное меню', font=("Times New Roman", 20), bg='#5CDB95', fg="#05386B")
title.place(x=60, y=10)

buyer = Button(window1, text='Покупатели', font=("Times New Roman", 13), bg="#05386B", fg="#EDF5E1", command=Buyer)
buyer.place(x=80, y=60)

seller = Button(window1, text='Продавцы', font=("Times New Roman", 13), bg="#05386B", fg="#EDF5E1", command=Seller)
seller.place(x=80, y=100)

realty = Button(window1, text='Недвижимость', font=("Times New Roman", 13), bg="#05386B", fg="#EDF5E1", command=Realty)
realty.place(x=80, y=140)

sale = Button(window1, text='Продажи', font=("Times New Roman", 13), bg="#05386B", fg="#EDF5E1")
sale.place(x=80, y=180)

tasks = Button(window1, text='Задачи', font=("Times New Roman", 13), bg="#05386B", fg="#EDF5E1", command=Tasks)
tasks.place(x=80, y=220)

report = Button(window1, text='Просмотреть отчёт', font=("Times New Roman", 13), bg="#05386B", fg="#EDF5E1", command=Report)
report.place(x=80, y=260)

window1.mainloop()