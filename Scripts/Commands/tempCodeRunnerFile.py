mod=Tk()
mod.title('Modifier la séléction')
Label(self.master, text='Nom et Prénom').grid(row=0, column=0)
Label(self.master, text='Note').grid(row=0, column=1)
Label(self.master, text='Redoublant').grid(row=0, column=2)
Label(self.master, text='Appréciations').grid(row=0, column=3)
'''i=0
for item in selection:
    for k in range(4):
        Entry(mod, text=tree.item(item)['values'][k]).grid(row=i,column=0)'''
mod.mainloop()