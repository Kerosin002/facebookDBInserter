import tkinter as tk
#from tkinter import Button, Label, Place, filedialog, Text, Entry
import os
from fbgpinsertFun import fbdbi

def insert():
    gpn=entryGN.get()
    print(gpn)
    link=entryGL.get()
    print(link)
    anon=var1.get()
    print(anon)
    fbdbi(gpn,link,anon)
    

root=tk.Tk()
root.configure(background="#263D42")
root.title("El-Time FBDBI")
scriptPath=os.path.realpath(__file__)
spsl=scriptPath.rfind("\\")
scDir=scriptPath[0:spsl]
icon="\\elico.ico"
icoPath=scDir+icon
root.iconbitmap(icoPath)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#root.geometry(f'{screen_width-200}x{screen_height-200}')
root.resizable(False,False)
root.rowconfigure(1, weight=0)
#root.columnconfigure(1,weight=1)
grtngs=tk.Label(root,text="Добро подаловать в El-Time FaceBook DataBase Inserter")
grtngs.grid(row=0,column=0,columnspan=2, sticky=tk.EW)
entryGN = tk.Entry(root) 
entryGL = tk.Entry(root, width=50) 
grpNL=tk.Label(root,text="Название группы:")
grpLL=tk.Label(root,text="Ссылка на группу")
var1=tk.IntVar()
anonCh = tk.Checkbutton(root, text='Группа с анон-постингом',variable=var1, onvalue=1, offvalue=0)
fbtn=tk.Button(master=root, text="Добавить Группу", padx=25,
                   pady=10, fg='#263D42', bg="red",command=insert)
grpNL.grid(row=1,column=0)
grpLL.grid(row=2,column=0)
entryGN.grid(row=1, column=1)
entryGL.grid(row=2, column=1)
anonCh.grid(row=3,column=0,columnspan=3)
fbtn.grid(row=4, column=0,columnspan=3)
root.mainloop()