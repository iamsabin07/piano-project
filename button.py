from tkinter import *

ws = Tk()
ws.title("Choose a song")
ws.geometry('500x500')
ws.config(bg='#5FB691')


def msg1():
    print(5)


Button(ws, text ='click me', command= msg1).pack(pady=10)
Button(ws, text ='click me', command= msg1).pack(pady=10)
Button(ws, text ='click me', command= msg1).pack(pady=10)
ws.mainloop()