
import tkinter as tk

root = tk.Tk()
root.title("Merhaba Tkinter")
root.geometry("300x150")

label = tk.Label(root, text="Merhaba Dünya!", font=("Arial", 14))
label.pack(pady=20)

root.mainloop()
