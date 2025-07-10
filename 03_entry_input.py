
import tkinter as tk

def goster():
    veri = entry.get()
    label.config(text=f"Girdi: {veri}")

root = tk.Tk()
root.title("Girdi Örneği")

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Göster", command=goster)
button.pack()

label = tk.Label(root, text="")
label.pack(pady=5)

root.mainloop()
