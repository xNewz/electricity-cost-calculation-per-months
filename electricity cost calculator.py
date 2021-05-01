from tkinter import *
from tkinter import messagebox

gui = Tk()
gui.title("คำนวนค่าไฟฟ้า ต่อเดือน")
gui.geometry("250x200")
gui.resizable(0,0)

def process():
    unit = float(string_unit.get())
    baht = int(string_baht.get())
    unit = unit * 30
    s = str(unit * baht)
    messagebox.showinfo("ผลการคำนวน", "ค่าไฟฟ้า " + s + " บาท")


string_unit = StringVar()
label_unit = Label(text="จำนวนที่ใช้ไปต่อเดือน / ยูนิต").pack(pady=10)
txt_unit = Entry(textvariable=string_unit).pack()

string_baht = StringVar()
label_baht = Label(text="บาท / ยูนิต").pack(pady=10)
txt_baht = Entry(textvariable=string_baht).pack()

btn = Button(text="คำนวน", command=process).pack(pady=10)
gui.mainloop()