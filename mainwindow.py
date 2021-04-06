from tkinter import *
from login import *
from tkinter import messagebox
from store import *
w = Tk()
w.geometry('500x500')
w.title('Ts Eamcet')
Label(w,text='TS EAMCET',height=3,bg='pink',fg='black').pack(fill = X)
Button(w,text='Register',height=3,width=20,command=register).pack()
Button(w,text='admitcard',height=3,width=20,command=login).pack()
w.mainloop()
