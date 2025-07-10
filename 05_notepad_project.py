
import tkinter as tk
from tkinter import filedialog

def kaydet():
    veri = text.get("1.0", tk.END)
    dosya_yolu = filedialog.asksaveasfilename(defaultextension=".txt")
    if dosya_yolu:
        with open(dosya_yolu, "w") as f:
            f.write(veri)

root = tk.Tk()
root.title("Not Defteri")

text = tk.Text(root)
text.pack(expand=True, fill="both")

button = tk.Button(root, text="Kaydet", command=kaydet)
button.pack()

root.mainloop()
