from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Checkbutton
import requests
from requests import post
from main import process

login = ''
password = ''

window = Tk()
window.title("Добро пожаловать в систему АСКУРБ")
window.geometry('380x130')


def clicked():
    # res = "Привет {}".format(login_ent.get())
    # login_lab.configure(text=res)
    if (True):   # Проверка на существование пользователя

        contacts_data = {
            "article":{
                "title": "PROVERKA3",
            "description": str(process),
            "body": "gyukyjg",
            "author_id": 1
        }}
        print(type(contacts_data))
        r = requests.post('http://127.0.0.1:8000/api/articles/', json=contacts_data)
        print(r.json())

        window.quit()
        messagebox.showinfo('Авторизация', 'Пользователь авторизован')


def show_info():
    messagebox.showinfo('Заголовок', 'ISPOLZOVANIE ISPOLZOVANIE ISPOLZOVANIE ISPOLZOVANIE ISPOLZOVANIE ISPOLZOVANIE')



def focus1(event):
    btn.focus_set()
def focus2(event):
    password_ent.focus_set()


login_lab = Label(window, text="Введите логин:")
login_lab.grid(column=0, row=0)
login_ent = Entry(window, width=20)
login_ent.grid(column=1, row=0)
login_ent.bind("<Return>", focus2)
login_ent.focus()

chk_state = BooleanVar()
chk_state.set(True)  # задайте проверку состояния чекбокса
lbl_ch = Label(window, text="Ознакомлен с условиями использования")
lbl_ch.grid(column=0, row=3)
chk = Checkbutton(window, var=chk_state)
chk.grid(column=1, row=3)

password_lab = Label(window, text="Введите пароль:")
password_lab.grid(column=0, row=1)
password_ent = Entry(window, width=20)
password_ent.grid(column=1, row=1)
password_ent.bind("<Return>", focus1)
btn = Button(window, text="Авторизоваться", width=15, height=3, command=clicked)
btn.grid(column=1, row=4)
btn_info = Button(window, text="Подробнее", width=15, height=3, command=show_info)
btn_info.grid(column=0, row=4)


window.mainloop()

