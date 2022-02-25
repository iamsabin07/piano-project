# Project: piano-project
# Author: Sabin Thapa
# Language: Python3
# Objective: To create a program to play automatically play piano in virtualpiano.net

import pyautogui as pg
import time
import webbrowser
from tkinter import *
from tkinter import messagebox

# create an instance of tkinter
ws = Tk()
ws.title("Choose a song")
ws.geometry('300x350')
ws.config(bg='#000000')


# method to end the program
def end():
    messagebox.showinfo('Info', 'Thank you for listening.')


# method to play virtual piano
def play(source, delay_period):
    # open the virtual piano in the website
    webbrowser.open_new("https://virtualpiano.net")
    # wait till the piano launches
    time.sleep(8)

    # feed the source music sheet
    with open(source) as sheet:
        # read the source music sheet
        notes = sheet.read()

        # initialize the index of the notes
        line_index = 0
        # loop the index until the end of the notes
        while line_index in range(len(notes)):
            # play the piano if the notes' string is alphabet or digit
            if notes[line_index].isalpha() or notes[line_index].isdigit():
                pg.press(notes[line_index])

            else:
                # wait till playing next note
                if notes[line_index] == '|':
                    time.sleep(delay_period * 16)

                # create a chord array to store chord notes
                if notes[line_index] == '[':
                    chord_array = []

                    while notes[line_index] != ']':
                        if notes[line_index].isalpha() or notes[line_index].isdigit():
                            chord_array.append(notes[line_index])
                        line_index += 1
                    # play the chord keys
                    exec('pg.hotkey(' + str(chord_array)[1: -1] + ')')
            time.sleep(delay_period)

            line_index += 1
    # end the program
    end()


# method to play River flows in you
def yiruma():
    # source file
    source = 'Yiruma_Sheet.txt'
    # delay period
    delay_period = 0.03
    # kill tkinter instance
    ws.destroy()
    # call play method
    play(source, delay_period)


def furelise():
    # source file
    source = 'Fur_Elise_Sheet.txt'
    # delay period
    delay_period = 0.07
    # kill tkinter instance
    ws.destroy()
    # call play method
    play(source, delay_period)


def interstellar():
    # source file
    source = 'Interstellar_Sheet.txt'
    # delay period
    delay_period = 0.1
    # kill tkinter instance
    ws.destroy()
    # call play method
    play(source, delay_period)


# create label in the instance of tkinter
label = Label(ws, text="Choose Any Song", height=1, width=15, bg='#000000', fg='white', font=('Calibri', 12))
label.pack(pady=20)
# create button in the instance of tkinter
Button(ws, text='River Flows in you', command=yiruma, height=1, width=15).pack(pady=20)
Button(ws, text='Fur Elise', command=furelise, height=1, width=15).pack(pady=20)
Button(ws, text='   Interstellar  ', command=interstellar, height=1, width=15).pack(pady=20)
# execute the instance of tkinter
ws.mainloop()
