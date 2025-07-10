
import tkinter as tk

def tikla():
    label.config(text="Tıkladın!")

root = tk.Tk()
root.title("Buton Örneği")

label = tk.Label(root, text="Henüz tıklanmadı")
label.pack(pady=10)

button = tk.Button(root, text="Tıkla", command=tikla)
button.pack()

root.mainloop()
