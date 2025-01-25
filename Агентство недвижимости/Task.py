import tkinter as tk
from tkinter import ttk, messagebox

import pyodbc
import datetime

def TaskWin():
    windowT = tk.Tk()
    windowT.title('Задачи')
    windowT.geometry('1450x750')
    windowT.configure(bg='#5CDB95')

    conn_str = (
        r'DRIVER={SQL Server};'
        r'SERVER=DESKTOP-KVMIVOD\SQLEXPRESS;'
        r'DATABASE=EstateAgency;'
        r'TRUSTED_CONNECTION=yes;'
    )
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    def display():
        global table
        try:
            for widget in windowT.winfo_children():
                if isinstance(widget, ttk.Treeview):
                    widget.destroy()
            cursor.execute("SELECT * FROM Tasks")
            rows = cursor.fetchall()
            table = ttk.Treeview(windowT, columns=['ID', 'Task', 'Deskription', 'Date', 'Place', 'Opponent'],
                                 show="headings")
            table.heading("ID", text="id")
            table.heading("Task", text="Задача")
            table.heading("Deskription", text="Описание задачи")
            table.heading("Date", text="Дата и время")
            table.heading("Place", text="Место выполнения")
            table.heading("Opponent", text="Оппонент")

            table.column("#1", width=0, stretch="no")
            table.column("#2", width=100)
            table.column("#3", width=300)
            table.column("#4", width=150)
            table.column("#5", width=300)
            table.column("#6", width=500)

            for row in rows:
                values = [str(value).replace("(", "").replace(")", "")
                          .replace(",", "") for value in row]
                table.insert("", tk.END, values=values)
            table.place(x=60, y=70)

        except pyodbc.Error:
            tk.messagebox.showerror("Ошибка", f"Ошибка при получении данных: {pyodbc.Error}")

####################################################################################################

    display()

    title = tk.Label(windowT, text='Запланированные задачи', font=("Times New Roman", 20), bg='#5CDB95', fg="#05386B")
    title.place(x=600, y=10)

    text_Task = tk.Label(windowT, text='Задача', font=("Times New Roman", 14), bg='#5CDB95', fg="#05386B")
    text_Task.place(x=250, y=350)
    entry_Task = tk.Entry(windowT)
    entry_Task.place(x=350, y=340, width=310, height=40)

    text_Description = tk.Label(windowT, text='Описание', font=("Times New Roman", 14), bg='#5CDB95', fg="#05386B")
    text_Description.place(x=250, y=430)
    entry_Description = tk.Entry(windowT)
    entry_Description.place(x=350, y=400, width=310, height=100)

    text_Date = tk.Label(windowT, text='Дата и время', font=("Times New Roman", 14), bg='#5CDB95', fg="#05386B")
    text_Date.place(x=225, y=525)
    entry_Date = tk.Entry(windowT)
    entry_Date.place(x=350, y=520, width=310, height=40)

    text_Place = tk.Label(windowT, text='Место', font=("Times New Roman", 14), bg='#5CDB95', fg="#05386B")
    text_Place.place(x=260, y=590)
    entry_Place = tk.Entry(windowT)
    entry_Place.place(x=350, y=580, width=310, height=40)

    text_Opponent = tk.Label(windowT, text='Оппонент', font=("Times New Roman", 14), bg='#5CDB95', fg="#05386B")
    text_Opponent.place(x=250, y=655)
    entry_Opponent = tk.Entry(windowT)
    entry_Opponent.place(x=350, y=645, width=310, height=40)

    home = tk.Button(windowT, text='В главное меню', font=("Times New Roman", 13), bg="#05386B", fg="#EDF5E1")
    home.place(x=1300, y=10, width=150, height=40)

    upd = tk.Button(windowT, text='Изменить', font=("Times New Roman", 15), bg="#05386B", fg="#EDF5E1")
    upd.place(x=900, y=400, width=150, height=40)

    save = tk.Button(windowT, text='Добавить', font=("Times New Roman", 15), bg="#05386B", fg="#EDF5E1")
    save.place(x=900, y=500, width=150, height=40)

    delete = tk.Button(windowT, text='Удалить', font=("Times New Roman", 15), bg="#05386B", fg="#EDF5E1")
    delete.place(x=900, y=600, width=150, height=40)



    windowT.mainloop()
    conn.close()
TaskWin()
