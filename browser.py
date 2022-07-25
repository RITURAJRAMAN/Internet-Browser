import pywhatkit
from tkinter import *

window = Tk()
window.title("By Rituraj Raman")
window.geometry('500x300')
window.configure(bg='black')
Label(window, text="Google Search", font="algerian 25 bold", fg='red', bg='black').place(x=75, y=20)
text = StringVar()
Label(window, text="Enter Your Text", font='arial 15 bold', fg='white', bg='black').place(x=30, y=100)
entry = Entry(window, textvariable=text, font='arial 16')
entry.place(x=30, y=140, width=430, height=35)


def search():
    x = text.get()
    pywhatkit.search(x)


Button(window, text="Search", font='arial 15 bold', bg='yellow', fg='blue', command=search).place(x=180, y=200)
window.mainloop()
