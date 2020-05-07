from tkinter import *
from tkinter import messagebox

tnt = Tk()

def function(value):
    if value == 'Log of':
        messagebox.askokcancel("Warning", "This will delete stuff")


menu = Frame(tnt)
menu.pack(pady = 5, padx = 50)
var = StringVar(tnt)

options = [
        'Enter',
        'Edit', 
        'Retrieve',
        'Report 1 - Dates of birth',
        'Report 2 - Home phone numbers',
        'Report 3 - Home addresses',
        'Log off',

]
option = OptionMenu(menu, var, options[0], *options, command=function)


def donothing():
   do = Tk()
   Label(do, text="up comming...").pack()
   
def winsecr():
    try:
        prauto = StringVar()
        prauto.set(NONE)
        winsecrr = Tk()
        RADIOBUTTON(winsecrr, text='on', Variable=prauto,value='pron').pack()
        RADIOBUTTON(winsecrr, text='off', Variable=prauto,value='proff').pack()
        winsecrr.mainloop()
    except:
        messagebox.showerror('there is a error','there is a error')
def open():
    def booring():
        messagebox.askyesno('warning','are you sure you want to open')
        tnt.title('booring')
        save.destroy()
    def super():
        messagebox.askyesno('warning','are you sure you want to open')
        tnt.title('super')
        save.destroy()
    save = Tk()
    Button(save, text='booring', command=booring).pack()
    Button(save, text='super', command=super).pack()
    save.mainloop()
def new():
    tnt.title('tk')

        


menubar =   Menu(tnt)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=open)
filemenu.add_command(label="Save", command=lambda: messagebox.showinfo('program saved','program saved'))
filemenu.add_command(label="Save as...", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=tnt.destroy)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="super secret settings", command=winsecr)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

tnt.config(menu=menubar)





def aboutwin():
    ab = Tk()
    Label(ab, text='this a costomizeble window').pack()
    Label(ab, text='you can costomize title').pack()
    ab.mainloop()


tnt.geometry('250x250')
 
Button(tnt, text='x', bg='red',command=tnt.destroy).pack()
title_entry = Entry(tnt, fg='blue')
title_entry.pack()
Button(tnt, text='set title', bg='blue', command=lambda: tnt.title(title_entry.get())).pack()




tnt.mainloop()
