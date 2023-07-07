#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 09:01:56 2023

@author: vishuddhimakeshwaran
"""

from tkinter import * 

root = Tk()
root.title("Encryption with ASCII")
root.geometry("400x500")

input_word = Entry(root)
input_word.place(relx = 0.5, rely = 0.3, anchor = CENTER)

label_ans = Label(root, text = "Name in ASCII is: ")
label_ans.place(relx = 0.5, rely = 0.5, anchor = CENTER)

label_ans2 = Label(root, text = "Encrypted name is: ")
label_ans2.place(relx = 0.5, rely = 0.6, anchor = CENTER)

def convertWord(): 
    word = input_word.get()
    for letter in word:
        num = ord(letter)
        label_ans["text"] += str(num) + " "
        num = num - 1
        label_ans2["text"] += chr(num) + " "

button1 = Button(root, text = "Covert into ASCII", command = convertWord)
button1.place(relx = 0.5, rely = 0.4, anchor = CENTER)

root.mainloop()