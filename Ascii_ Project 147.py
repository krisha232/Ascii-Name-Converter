# -*- coding: utf-8 -*-
from tkinter import *

root=Tk()
root.title("Ascii")
root.geometry("400x400")
root.configure(background='snow')


enter_word=Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)
label=Label(root, text="Name In Ascii : ", bg="lightblue", fg="black")
encryption_label=Label(root, text="Encrypted Name : ", bg="lightblue", fg="black")

def asciiConverter():
    input_word = enter_word.get()
    
    for letter in input_word :
        label["text"] +=str(ord(letter)) + " "
        encrypt =int(ord(letter)) 
        final = encrypt - 1
        encryption_label["text"] += str(chr(final)) + " "
        
btn=Button(root, text="Show Name In Ascii & Encrypted Value",command=asciiConverter,bg='gold', fg='black')
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

label.place(relx=0.5,rely=0.6,anchor=CENTER)
encryption_label.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()