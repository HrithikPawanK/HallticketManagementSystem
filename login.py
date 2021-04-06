from tkinter import *
from random import *
from tkinter import messagebox
from store import *
def error1():
  root = Tk()
  root.withdraw()
  messagebox.showerror("Error", "wrong password")
def error2():
  root = Tk()
  root.withdraw()
  messagebox.showerror("Error", "wrong application number")
def login():
    global username
    global dob
    Label(text='Please enter your details below to login')
    l_w = Toplevel()
    l_w.geometry('300x300')
    l_w.title('admitcard')
    Label(l_w,text='USERNAME:').pack()
    username = Entry(l_w)
    username.pack()
    Label(l_w,text='PASSWORD').pack()
    dob = Entry(l_w)
    dob.pack()
    Button(l_w,text='Login',bg = 'blue',fg = 'white',command = login_verify).pack()
def login_verify():
    global u
    global d
    f = open('info_f.txt','r')
    u = username.get()
    d = dob.get()
    global count
    count = 0
    global info
    while(1):
        y = f.readline()
        x = y.split(';')
        if x[0] == u:
            count += 1
            if x[1] == d:
                info = x
                admitcard(info)
            else:
                error1()
        if y == '':
            break
    if count == 0:
        error2()
def admitcard(a):
    center = ['ION DIGITAL HAYATHNAGAR','ION DIGITAL LBNAGAR','ION DIGITAL NACHARAM']
    time = {0:'9:30 to 12:30',1:'2:30 to 5:30'}
    appno = 'TS' + '2k19' + '%04d'%(randint(0,9999))
    hallticket = Toplevel()
    hallticket.geometry('600x400')
    hallticket.title('Admitcard')
    Label(hallticket,text='TS EAMCET 2k19',bg = 'pink',fg='black',height=5,width=60).grid(row=0,columnspan=10)
    d = ["candidate's name:","father's name:","mother's name:",'date of birth:','email:','phone:','address:']
    Label(hallticket,text="candidate's name:").grid(row=1,column=0,sticky=W)
    Label(hallticket,text=a[0]).grid(row=1,column=1,sticky=W)
    Label(hallticket, text="father's name:").grid(row=2,column=0,sticky=W)
    Label(hallticket, text=a[3]).grid(row=2,column=1,sticky=W)
    Label(hallticket,text="mother's name:").grid(row=3,column=0,sticky=W)
    Label(hallticket, text=a[4]).grid(row=3, column=1, sticky=W)
    Label(hallticket,text='date of birth:').grid(row=4,column=0,sticky=W)
    Label(hallticket, text=a[1]).grid(row=4, column=1, sticky=W)
    Label(hallticket, text='email:').grid(row=5,column=0,sticky=W)
    Label(hallticket, text=a[5]).grid(row=5, column=1, sticky=W)
    Label(hallticket, text='phone:').grid(row=6,column=0,sticky=W)
    Label(hallticket, text=a[6]).grid(row=6, column=1, sticky=W)
    Label(hallticket, text='address:').grid(row=7,column=0,sticky=W)
    Label(hallticket, text=a[7]).grid(row=7, column=1, sticky=W)
    Label(hallticket,text='Gender:').grid(row=1,column=2)
    Label(hallticket,text=a[2]).grid(row=2,column=2)
    Label(hallticket,text='Hallticket:').grid(row=1,column=3)
    Label(hallticket,text=appno).grid(row=2,column=3)
    f = open('hp.txt','w')
    f.write(a[8])
    x = a[8][:-1]
    photo = PhotoImage(file=x)
    Label(hallticket,image=photo).grid(row=3,column=4,columnspan=4,rowspan=4)
    i = randint(0,2)
    j = randint(0,1)
    Label(hallticket,text='Center').grid(row=9,column=3)
    Label(hallticket,text='date: 22/05,2019').grid(row=10,column=0,columnspan = 2)
    Label(hallticket,text='time: '+ time[j]).grid(row=9,column=0,columnspan = 2)
    Label(hallticket,text=center[i]).grid(row=10,column=3,columnspan=2)
    hallticket.mainloop()
