import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import os

db_path = os.path.join(os.path.split(os.path.split(os.path.dirname(__file__))[0])[0],'data\Marks.db')

db = sqlite3.connect(db_path)
db.row_factory=sqlite3.Row
result = db.execute('SELECT * FROM Marks')
L=[]
for row in result:
    T=[]
    T.append(row['ID'])
    T.append(row['Nom'])
    T.append(row['Note'])
    T.append(row['Redoublant'])
    T.append(row['Comment'])
    L.append(T)
db.commit()
db.close()

master = Tk()
tree = ttk.Treeview(master)
tree["columns"]=("Nom", "Note", "Redoublant", "Comment")
tree.column("#0", width=40, minwidth=40, stretch=NO)
tree.column("#1", width=200, minwidth=100, stretch=NO)
tree.column("#2", width=40, minwidth=50, stretch=NO)
tree.column("#3", width=70, minwidth=70, stretch=NO)
tree.column("#4", width=400, minwidth=80, stretch=NO)
tree.heading("#0", text="ID",anchor=CENTER)
tree.heading("#1", text="Nom",anchor=CENTER)
tree.heading("#2", text="Note",anchor=CENTER)
tree.heading("#3", text="Redoublant",anchor=CENTER)
tree.heading("#4", text="Appréciations",anchor=CENTER)
for row in L:
    tree.insert('', 'end', text=row[0], values=(row[1],row[2],row[3],row[4]))
tree.pack()
def selection_msg():
    messagebox.showinfo('',tree.selection())
    for item in tree.selection():
        print(type(tree.item(item)))
        print(tree.item(item))
Button(master,text='s',command=selection_msg).pack()
def sel():
    print(tree.item(tree.focus()))
    print(tree.focus())
Button(master, text='f', command=sel).pack()
master.mainloop()
'''
import tkinter as tk
from tkinter import ttk, Tk


def insert(tree, value):
    tree.insert('', tk.END, value, text=value)

root = Tk()
tree = ttk.Treeview(root)

insert(tree, '1')
insert(tree, '2')
insert(tree, '3')

tree.pack()
children = tree.get_children() 
tree.selection_set(children)
tree.selection_toggle(children[1])

# uncomment line by line to see the change
#tree.selection_toggle(children)
#tree.selection_remove(children[1])

print(tree.selection())

root.mainloop()'''