import tkinter as tk
from PIL import Image, ImageTk

logo = Image.open('logo3.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)