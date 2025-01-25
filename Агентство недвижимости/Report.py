import tkinter as tk
from tkinter import ttk
import pyodbc
import pandas as pd

def ReportWin():
    window4 = tk.Tk()
    window4.title('Отчёт')
    window4.geometry('1200x350')

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
        """Выводит данные из SQL Server в таблицу Tkinter."""
        try:
            # очистка таблицы
            for widget in window4.winfo_children():
                if isinstance(widget, ttk.Treeview):
                    widget.destroy()
            cursor.execute("select d.ID, a.FIO, b.FIO, c.Address, d.Date, d.Price from Buyer a, Seller b, Realty c, Report d where d.ID_Buyer = a.ID and d.ID_Seller = b.ID and d.ID_Realty = c.ID")
            rows = cursor.fetchall()

            # Создаем таблицу Tkinter
            table = ttk.Treeview(window4, columns=['ID', 'ID_Buyer', 'ID_Seller', 'ID_Realty', 'Date', 'Price'], show="headings")

            table.heading("ID", text="id")
            table.heading("ID_Buyer", text="Покупатль")
            table.heading("ID_Seller", text="Продавец")
            table.heading("ID_Realty", text="Адрес")
            table.heading("Date", text="Дата сделки")
            table.heading("Price", text="Цена")

            table.column('#1', width=40)
            table.column('#2', width=250)
            table.column('#3', width=250)
            table.column('#4', width=400)
            table.column('#5', width=80)
            table.column('#6', width=100)

            scrollbar = tk.Scrollbar(window4, orient="vertical", command=table.yview)
            table['yscrollcommand'] = scrollbar.set
            scrollbar.pack(side="right", fill="y")

            # Заполняем таблицу данными
            for row in rows:
                values = [str(value).replace("(", "").replace(")", "").replace(",", "") for value in row]
                table.insert("", tk.END, values=values)
            table.pack()


        except pyodbc.Error:
            tk.messagebox.showerror("Ошибка", f"Ошибка при получении данных: {pyodbc.Error}")

    def Save_to_excel():
        cursor.execute(
            "select d.ID, a.FIO, b.FIO, c.Address, d.Date, d.Price from Buyer a, Seller b, Realty c, Report d where d.ID_Buyer = a.ID and d.ID_Seller = b.ID and d.ID_Realty = c.ID")
        rows = cursor.fetchall()

        # Создаем DataFrame с данными из SQL запроса
        df = pd.DataFrame.from_records(rows, columns=['ID', 'Покупатель', 'Продавец', 'Адрес', 'Дата сделки', 'Цена'])

        # Сохраняем данные в Excel файл
        df.to_excel('report.xlsx', index=False)
        tk.messagebox.showinfo("Успех", "Данные сохранены в файл report.xlsx")

    display()

    save_button = tk.Button(window4, text="Сохранить в Excel", command=Save_to_excel)
    save_button.place(x=570, y=250)

    window4.mainloop()
    conn.close()