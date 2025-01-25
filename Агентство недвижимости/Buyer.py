import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc ##библиотека для работы с СУБД
import datetime
def BuyerWin():
    window3 = tk.Tk()
    window3.title('Покупатели')
    window3.geometry('1300x1250')

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
            for widget in window3.winfo_children():
                if isinstance(widget, ttk.Treeview):
                    widget.destroy()
            cursor.execute("SELECT * FROM Buyer")
            rows = cursor.fetchall()

            # Создаем таблицу Tkinter
            table = ttk.Treeview(window3, columns=['ID', 'FIO', 'Price_range', 'Wishes', 'Date_of_application', 'Telephone'], show="headings")

            table.heading("ID", text="id")
            table.heading("FIO", text="ФИО")
            table.heading("Price_range", text="Диапазон цены")
            table.heading("Wishes", text="Пожелания")
            table.heading("Date_of_application", text="Дата обращения")
            table.heading("Telephone", text="Номер телефона")

            table.column('#1', width=40)
            table.column('#4', width=400)

            scrollbar = tk.Scrollbar(window3, orient="vertical", command=table.yview)
            table['yscrollcommand'] = scrollbar.set
            scrollbar.pack(side="right", fill="y")

            # Заполняем таблицу данными
            for row in rows:
                values = [str(value).replace("(", "").replace(")", "").replace(",", "") for value in row]
                table.insert("", tk.END, values=values)
            table.pack()

        except pyodbc.Error:
            tk.messagebox.showerror("Ошибка", f"Ошибка при получении данных: {pyodbc.Error}")

    def Delete():
        selected_item = table.focus()  # получаем выбранный элемент в таблице
        data = table.item(selected_item)
        try:
            id = data['values'][0]  # получаем ID выбранной строки
            cursor.execute(f"DELETE FROM Buyer WHERE ID = ?", (id))
            conn.commit()
            display()
        except IndexError:
            messagebox.showerror("Ошибка", "Выберите строку для удаления")

    def Add():
        start = datetime.datetime.now()
        try:
            FIO = entry_FIO.get()
            Price_range = entry_Price_range.get()
            Wishes = entry_Wishes.get()
            Date_of_application = entry_Date_of_application.get()
            Telephone = entry_Telephone.get()
            cursor.execute(f'insert into Buyer (FIO, Price_range, Wishes, Date_of_application, Telephone) values (?, ?, ?, ?, ?)', (FIO, Price_range, Wishes, Date_of_application, Telephone))
            conn.commit()

            entry_FIO.delete(0, tk.END)
            entry_Price_range.delete(0, tk.END)
            entry_Wishes.delete(0, tk.END)
            entry_Date_of_application.delete(0, tk.END)
            entry_Telephone.delete(0, tk.END)

            display()
        except pyodbc.Error:
            messagebox.showerror("Ошибка", f"Ошибка при добавлении данных: {pyodbc.Error}")
        finish = datetime.datetime.now()
        print(str(finish-start))

    def Update():
        update.place(x=780, y=500)
        save.place_forget()

        select = table.selection()[0]  ## выбрать выделенные данные из таблицы
        values = table.item(select, "values")

        # Всавить данные по столбцам
        entry_FIO.delete(0, tk.END)
        entry_FIO.insert(0, values[1])

        entry_Price_range.delete(0, tk.END)
        entry_Price_range.insert(0, values[2])

        entry_Wishes.delete(0, tk.END)
        entry_Wishes.insert(0, values[3])

        entry_Date_of_application.delete(0, tk.END)
        entry_Date_of_application.insert(0, values[4])

        entry_Telephone.delete(0, tk.END)
        entry_Telephone.insert(0, values[5])


    def Upd():
        update.place_forget()
        save.place(x=700, y=500)
####################################################################################################

    display()

    upd = ttk.Button(window3, text='Изменить', command=Update)
    upd.place(x=400, y=240)

    text_FIO = tk.Label(window3, text='ФИО')
    text_FIO.place(x=100, y=350)
    entry_FIO = tk.Entry(window3)
    entry_FIO.place(x=150, y=340, width=310, height=40)

    text_Price_range = tk.Label(window3, text='Диапазон цены')
    text_Price_range.place(x=32, y=400)
    entry_Price_range = tk.Entry(window3)
    entry_Price_range.place(x=150, y=390, width=310, height=40)

    text_Wishes = tk.Label(window3, text='Пожеления')
    text_Wishes.place(x=50, y=450)
    entry_Wishes = tk.Entry(window3)
    entry_Wishes.place(x=150, y=440, width=310, height=320)

    text_Date_of_application = tk.Label(window3, text='Дата обращения')
    text_Date_of_application.place(x=600, y=350)
    entry_Date_of_application = tk.Entry(window3)
    entry_Date_of_application.place(x=710, y=340, width=310, height=40)

    text_Telephone = tk.Label(window3, text='Номер телефона')
    text_Telephone.place(x=600, y=400)
    entry_Telephone = tk.Entry(window3)
    entry_Telephone.place(x=710, y=390, width=310, height=40)

    save = tk.Button(window3, text='Добавить', command=Add)
    save.place(x=700, y=500)

    update = tk.Button(window3, text='Изменить', command=Upd)
    update.place_forget()


    delete = tk.Button(window3, text='Удалить', command=Delete)
    delete.place(x=600, y=240)



    window3.mainloop()
    conn.close()
