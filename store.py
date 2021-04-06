from tkinter import *
class candidate:
    def candidate_tk(self):
        self.c = Tk()
        self.c.geometry('250x250')
        self.c.title('Application Form')
        info = ['name','Gender','Dob','f_name','m_name','email','phone','address','photo_dir']
        global l
        l = []
        for i in range(len(info)):
            temp = Label(self.c,text=info[i])
            temp.grid(row=i,column=0,columnspan=2,sticky=E)
            l.append(Entry(self.c))
            l[i].grid(row=i,column=2,columnspan=2)
        Button(self.c,text='Apply',height=1,width=25,bg='blue',fg='white',command=self.info_f).grid(row=i+1,column=2)
        self.c.mainloop()
    def info_f(self):
        self.name = l[0].get();self.Gender = l[1].get();self.Dob = l[2].get();self.f_name = l[3].get();self.m_name = l[4].get();self.email = l[5].get();self.phone = l[6].get();self.address = l[7].get();
        self.photo_dir = l[8].get()
        f = open('info_f.txt', 'a')
        f.write(self.name + ';');f.write(self.Dob + ';');f.write(self.Gender + ';');f.write(self.f_name + ';');f.write(self.m_name + ';')
        f.write(self.email + ';');f.write(self.phone + ';');f.write(self.address + ';');f.write(self.photo_dir + '\n')
        f.close()
global s
s = list()
def register():
    s.append(candidate())
    s[len(s)-1].candidate_tk()




