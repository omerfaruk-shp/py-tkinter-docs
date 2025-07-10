
import tkinter as tk
from tkinter import Menu

def cikis():
    root.quit()

root = tk.Tk()
root.title("Menü Örneği")

menubar = Menu(root)
dosya_menu = Menu(menubar, tearoff=0)
dosya_menu.add_command(label="Yeni")
dosya_menu.add_separator()
dosya_menu.add_command(label="Çık", command=cikis)

menubar.add_cascade(label="Dosya", menu=dosya_menu)
root.config(menu=menubar)

root.mainloop()
