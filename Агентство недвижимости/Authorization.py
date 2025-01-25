import tkinter as tk
import pyodbc

def authenticate():
    login = login_entry.get()
    password = password_entry.get()

    conn_str = (
        r'DRIVER={SQL Server};'
        r'SERVER=DESKTOP-KVMIVOD\SQLEXPRESS;'
        r'DATABASE=EstateAgency;'
        r'TRUSTED_CONNECTION=yes;'
    )

    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Auth WHERE Login = ? AND Password = ?", (login, password))
    result = cursor.fetchone()

    conn.close()

    if result:
        auth_window.destroy()
        #
    else:
        error_label.config(text="Неверный ввод")

auth_window = tk.Tk()
auth_window.title("Авторизация")
auth_window.geometry("250x200")

login_label = tk.Label(auth_window, text="Логин:")
login_label.grid(row=0, column=0, padx=10, pady=10)

login_entry = tk.Entry(auth_window)
login_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(auth_window, text="Пароль:")
password_label.grid(row=1, column=0, padx=10, pady=10)

password_entry = tk.Entry(auth_window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

auth_button = tk.Button(auth_window, text="Войти", command=authenticate)
auth_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

error_label = tk.Label(auth_window, text="", fg="red")
error_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


auth_window.mainloop()