from tkinter import *
from tkinter import ttk
from ..Commands.SQLrequests import *

class Interface:
    def __init__(self, master):
        self.master = master
        self.style()
        self.name()
        self.note()
        self.redoublant()
        self.appreciation()
        self.buttons()
        
    def style(self):
        style = ttk.Style()
        style.configure("default", foreground="black", background="white")

    def name(self):
        Label(self.master, text='Nom et Prénom:').grid(row=0, column=0)
        self.name_entry = Entry(self.master)
        self.name_entry.grid(row=0, column=1, columnspan=2)

    def note(self):
        Label(self.master, text='Note:').grid(row=1, column=0)
        self.note_entry = Entry(self.master)
        self.note_entry.grid(row=1, column=1, columnspan=2)

    def redoublant(self):
        self.redoublant_choix = StringVar()
        self.redoublant_choix.set(NONE)
        Label(self.master, text='Redoublant:').grid(row=2, column=0)
        ttk.Radiobutton(self.master, text='Oui', variable=self.redoublant_choix, value='Oui').grid(row=2, column=1) 
        ttk.Radiobutton(self.master, text='Non', variable=self.redoublant_choix, value='Non').grid(row=2, column=2)
    
    def appreciation(self):
        Label(self.master, text='Appréciations:').grid(row=3, column=0)
        self.appreciation_text = Text(self.master, width=15, height=15)
        self.appreciation_text.grid(row=3, column=1, columnspan=2)

    def buttons(self):
        req=SQLrequests()
        ttk.Button(self.master, text='Liste des notes', command=lambda :self.tree()).grid(row=4, column=1)
        ttk.Button(self.master,text='Ajouter', command=lambda: req.ajouter(self.name_entry.get(), self.note_entry.get(),\
            self.redoublant_choix.get(), self.appreciation_text.get(1.0, END))).grid(row=4, column=2)
        ttk.Button(self.master, text='Clear', command=lambda :req.clear_table()).grid(row=4, column=0)
    
    def tree(self):
        req=SQLrequests()
        tree_master = Tk()
        tree_master.title('Liste des notes')
        tree = ttk.Treeview(tree_master)
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
        for row in req.get_list():
            tree.insert('', 'end', text=row[0], values=(row[1],row[2],row[3],row[4]))
        tree.pack()
        def suppr():
            for item in tree.selection():
                req.supprimer(tree.item(item)['text'])
                tree.delete(item)
        ttk.Button(tree_master, text='Supprimer', command=suppr).pack(side=RIGHT)
        def mod(focus):
            if focus == '':
                messagebox.showerror('Erreur','Veuillez choisir une ligne')
            else:
                mod=Tk()
                mod.title('Modifier la séléction')
                Label(mod, text='ID').grid(row=0, column=0)
                Label(mod, text='Nom et Prénom').grid(row=0, column=1)
                Label(mod, text='Note').grid(row=0, column=2)
                Label(mod, text='Redoublant').grid(row=0, column=3)
                Label(mod, text='Appréciations').grid(row=0, column=4)
                ttk.Label(mod, text=tree.item(focus)['text']).grid(row=1, column=0)
                Id = tree.item(focus)['text']
                L=[]
                for k in range(4):
                    e = ttk.Entry(mod)
                    e.grid(row=1,column=k+1)
                    e.insert(0, tree.item(focus)['values'][k]) 
                    L.append(e)
                tree_master.destroy()            
                def OK():
                    req.modifier(Id, L[0].get(), L[1].get(), L[2].get(), L[3].get())
                    mod.destroy()
                    self.tree()
                ttk.Button(mod, text='OK', command=OK).grid(row=2,column=4)
                mod.mainloop()
        ttk.Button(tree_master, text='Modifier', command=lambda: mod(tree.focus())).pack(side=RIGHT)
        tree_master.mainloop()
