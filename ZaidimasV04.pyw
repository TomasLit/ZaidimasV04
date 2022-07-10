import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

root.resizable(width=False, height=False)

root.title("Žaidimas Kas? Kur? Kada?")

canvas = tk.Canvas(root, width=400, height=250)
canvas.grid(columnspan=3, rowspan=1)

import Pictures

from tkinter import *

def zaisk():
    new3 = Toplevel(root)
    new3.title("Žaidimas Kas? Kur? Kada?")
    new3.geometry('400x220')

    label_1 = tk.Label(master=new3, text="Atsakykite į klausimus:")
    label_1.grid(column=2, row=0)

    label_kada = tk.Label(master = new3, text = "Kada?")
    label_kada.grid(column = 1, row = 1, sticky = "e")
    text_kada = tk.Entry(master = new3, width = 55)
    text_kada.grid(column=2, row=1)
    
    label_kas = tk.Label(master = new3, text = "Kas?")
    label_kas.grid(column = 1, row = 2, sticky = tk.E)
    text_kas = tk.Entry(master=new3, width = 55)
    text_kas.grid(column=2, row=2)

    lbl_ka = tk.Label(master = new3, text="Ką?")
    lbl_ka.grid(column=1, row=3, sticky="e")
    text_ka = tk.Entry(master=new3, width=55)
    text_ka.grid(column=2, row=3)

    import random
    import Data as D
    
    a = D.a
    Kur = random.choice(a)
    
    b = D.b
    Su_kuo = random.choice(b)
        
    c = D.c
    Ka_veikia = random.choice(c)
    
    txt ="{}, {} {} su {} {} {} \n"

    def ats():
        
        framet = tk.Frame(master=new3, height=5)
        framet.grid(column=2, row=6)

        frame4 = tk.Frame(
            master=new3, 
            width=320, 
            height=105, 
            )
        frame4.grid(column=2, row=8)

        browse_text.set("Jūsų žaidimo atsakymas:")

        label_ats = tk.Label(
            master=frame4, 
            text=txt.format(
                text_kada.get(), 
                Kur, 
                text_kas.get(), 
                Su_kuo, 
                Ka_veikia, 
                text_ka.get()), 
                borderwidth= 10, 
                font="Arial 12 bold", 
                fg="red",
                wraplength=300,
                justify='center'
                )
        label_ats.grid(column= 2, row=1, sticky="nsew")

        text=txt.format(
                text_kada.get(), 
                Kur, 
                text_kas.get(), 
                Su_kuo, 
                Ka_veikia, 
                text_ka.get())
               
        import mysql.connector
        db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "3214",
        database="zaidimo_istorija"
        )
        
        crsr = db.cursor()

        crsr.execute("CREATE DATABASE IF NOT EXISTS zaidimo_istorija")

        crsr.execute("CREATE TABLE IF NOT EXISTS istorija (name VARCHAR(255))")

        sqlFormula = "INSERT INTO istorija (name) VALUES (%s)"
        istorija = [text]

        crsr.execute(sqlFormula, istorija)
        db.commit()

    framet = tk.Frame(master=new3, height=5)
    framet.grid(column=2, row=4)

    browse_text = tk.StringVar()
    btn_submit = tk.Button(
        master=new3, 
        textvariable=browse_text,
        command=lambda:ats(),
        padx=5
        )
    browse_text.set("Pateikti atsakymus")
    btn_submit.grid(column=2, row=5)

def skaityk():
          
    import mysql.connector
    db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "3214",
    database="zaidimo_istorija"
    )
    
    crsr = db.cursor()
    crsr.execute("SELECT * FROM istorija")
    myresult = crsr.fetchall()
        
    new = Toplevel(root)
    new.title("Žaidimo istorija")
    
    label_skaityk = tk.Label(new, text = myresult, padx=5, pady=5)
    label_skaityk.pack()

def trink():
    
    import mysql.connector
    db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "3214",
    database="zaidimo_istorija"
    )

    crsr = db.cursor()
    sql = "DROP TABLE IF EXISTS istorija"
    crsr.execute(sql)
    db.commit()
        
def iseik():
    root.destroy()

frame1 = tk.Frame(master=root, width=400, height=300, padx=5, pady=5)
frame1.grid(columnspan=3, rowspan=7)

frame2 = tk.Frame(master=frame1, width=5, height=5)
frame2.grid(column=2, row=1)

button1 = tk.Button(
    master=frame1, 
    text="Žaisti žaidimą", 
    command=lambda:zaisk(), 
    font="Arial 12", 
    width=18, 
    height=3, 
    fg="gray"
    )
button1.config(bd=10, relief=RAISED)
button1.grid(column=1, row=0)
button2 = tk.Button(
    master=frame1, 
    text="Peržiūrėti ankstesnių\nžaidimų rezultatus", 
    command=lambda:skaityk(), 
    font="Arial", 
    width=18, 
    height=3,
    fg="gray"
    )
button2.config(bd=10, relief=RAISED)
button2.grid(column=1, row=2)
button3 = tk.Button(
    master=frame1, 
    text="Ištrinti buvusių\nžaidimų istoriją", 
    command=lambda:trink(), 
    font="Arial", 
    width=18, 
    height=3, 
    fg="gray"
    )
button3.config(bd=10, relief=RAISED)
button3.grid(column=3, row=0)
button4 = tk.Button(
    master=frame1, 
    text="Išeiti iš žaidimo", 
    command=lambda:iseik(),
    font="Arial", 
    width=18, 
    height=3, 
    fg="gray"
    )
button4.config(bd=10, relief=RAISED)
button4.grid(column=3, row=2)

root.mainloop()