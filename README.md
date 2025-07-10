# py-tkinter-docs
python tkinter dökümanları

![Hacker Cat](https://media.tenor.com/PLIr_VkF6ywAAAAM/ghostedvpn-hacker-cat.gif)

# 🐍 Tkinter GUI - Python ile Masaüstü Uygulama Geliştirme

> Tkinter, Python’un standart GUI kütüphanesidir. Windows, macOS ve Linux üzerinde çalışır. Kolay kullanımı sayesinde başlangıç ve orta seviye projeler için oldukça uygundur.

---

## 🚀 Başlangıç: Basit Bir Pencere

```python
import tkinter as tk

pencere = tk.Tk()
pencere.title("Merhaba Tkinter")
pencere.geometry("300x200")
pencere.mainloop()
```

---

## 🧱 Temel Tkinter Widget'ları

| Widget        | Açıklama                                |
|---------------|------------------------------------------|
| `Label`       | Metin gösterimi                         |
| `Button`      | Buton oluşturur                         |
| `Entry`       | Tek satır kullanıcı girişi              |
| `Text`        | Çok satırlı metin alanı                 |
| `Frame`       | Diğer widget'ları gruplar               |
| `Checkbutton` | Onay kutusu                             |
| `Radiobutton` | Radyo butonu                            |
| `Listbox`     | Liste kutusu                            |
| `Canvas`      | Grafik çizimi, şekiller                 |
| `Scale`       | Kaydırıcı (slider)                      |
| `Menu`        | Menü barı                               |

---

## 📌 Örnek: Label ve Button

```python
import tkinter as tk

def tikla():
    etiket.config(text="Butona tıkladın!")

pencere = tk.Tk()
etiket = tk.Label(pencere, text="Merhaba!", font=("Arial", 14))
etiket.pack(pady=10)

buton = tk.Button(pencere, text="Tıkla", command=tikla)
buton.pack()

pencere.mainloop()
```

---

## 🖊️ Entry (Giriş Alanı) Kullanımı

```python
from tkinter import *

def yazdir():
    giris = entry.get()
    etiket.config(text=f"Girdi: {giris}")

pencere = Tk()
entry = Entry(pencere)
entry.pack()

buton = Button(pencere, text="Göster", command=yazdir)
buton.pack()

etiket = Label(pencere, text="")
etiket.pack()

pencere.mainloop()
```

---

## 🎨 Renk, Yazı Tipi ve Stil

```python
etiket = Label(pencere, text="Stil Deneme", bg="lightblue", fg="darkred", font=("Helvetica", 16, "bold italic"))
etiket.pack()
```

---

## 📁 Menü ve Alt Menü

```python
from tkinter import *

def cikis():
    pencere.quit()

pencere = Tk()
menubar = Menu(pencere)

dosya = Menu(menubar, tearoff=0)
dosya.add_command(label="Yeni")
dosya.add_command(label="Kaydet")
dosya.add_separator()
dosya.add_command(label="Çıkış", command=cikis)

menubar.add_cascade(label="Dosya", menu=dosya)
pencere.config(menu=menubar)

pencere.mainloop()
```

---

## 🧭 Geometri Yöneticileri

Tkinter'da 3 ana yerleşim yöntemi vardır:

1. `.pack()` – Basit ve dikey/hiyerarşik yerleşim
2. `.grid(row, column)` – Satır/sütun tabanlı
3. `.place(x=, y=)` – Koordinat tabanlı

```python
buton1 = Button(pencere, text="A")
buton1.grid(row=0, column=0)
```

---

## ⏳ after() ile Zamanlayıcı

```python
def sayac(saniye):
    if saniye >= 0:
        etiket.config(text=str(saniye))
        pencere.after(1000, sayac, saniye - 1)

etiket = Label(pencere)
etiket.pack()
sayac(5)
```

---

## 🔁 Olaylar ve `bind()` Fonksiyonu

```python
def tus_basildi(event):
    etiket.config(text=f"Basılan tuş: {event.char}")

pencere.bind("<Key>", tus_basildi)
```

---

## 🧪 Mini Proje: Basit Not Defteri

```python
from tkinter import *

def kaydet():
    veri = metin.get("1.0", END)
    with open("notlar.txt", "w") as dosya:
        dosya.write(veri)

pencere = Tk()
pencere.title("Not Defteri")

metin = Text(pencere)
metin.pack()

buton = Button(pencere, text="Kaydet", command=kaydet)
buton.pack()

pencere.mainloop()
```

---

## 💡 İpuçları

- `mainloop()` GUI’yi sürekli aktif tutar.
- `destroy()` → pencereyi kapatır.
- `ttk` modülü ile modern temalar uygulanabilir.
- `tkinter.messagebox` ile popup pencereler oluşturabilirsin.
- Tüm widget'lar `.config()` ile dinamik olarak değiştirilebilir.

---

## 🔗 Kaynaklar

- [📘 GeeksforGeeks - Tkinter GUI](https://www.geeksforgeeks.org/python/python-gui-tkinter/)
- [📘 Python Docs - Tkinter](https://docs.python.org/3/library/tk.html)
- [🌐 TkDocs - Modern Tkinter](https://tkdocs.com)

---

## 👨‍💻 Yazar

**@omerfaruk-shp**  

📦 PHP • JS • Python  
🌍 GitHub: [github.com/omerfaruk-shp](https://github.com/omerfaruk-shp)
