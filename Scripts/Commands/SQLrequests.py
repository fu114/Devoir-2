import sqlite3
from tkinter import *
from tkinter import messagebox
import os


class SQLrequests:
    DB_PATH = os.path.join(os.path.split(os.path.split(os.path.dirname(__file__))[0])[0],'data\Marks.db')
    
    def __init__(self, db_path):
        self.db_path = db_path
        self.db = sqlite3.connect(self.db_path)
        self.db.execute('CREATE TABLE if NOT EXISTS Marks(\
            "ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
            "Nom"	VARCHAR(20),\
            "Note"	DECIMAL,\
            "Redoublant"	VARCHAR(3),\
            "Comment"	TEXT,\
            CONSTRAINT CHK_Redoublant CHECK (Redoublant=\'Oui\' or Redoublant=\'Non\')\
            )')
        self.db.commit()
        self.db.close()

    def __init__(self):
        self.db_path = self.DB_PATH

    def ajouter(self, name, note, redoublant, appreciation):
        try:
            if name == '' or redoublant == 'none' or appreciation == '' or note == '':
                messagebox.showwarning('Attention', 'Veuillez remplir toutes les cases')
            else:
                self.db = sqlite3.connect(self.db_path)
                self.db.execute('INSERT INTO Marks (Nom, Note, Redoublant, Comment) \
                                VALUES (\"{}\", {}, \"{}\", \"{}\")'.format(name, note, redoublant, appreciation))
                self.db.commit()
                self.db.close()
                messagebox.showinfo('Nouvel ajout','Ajout avec succès')
        except Exception as e:
            messagebox.showerror('Erreur', 'Erreur: {}'.format(e))
    
    def clear_table(self):
        self.db = sqlite3.connect(self.db_path)
        self.db.execute('DROP TABLE Marks')
        self.db.execute('CREATE TABLE Marks(\
                        "ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
                        "Nom"	VARCHAR(20),\
                        "Note"	DECIMAL,\
                        "Redoublant"	VARCHAR(3),\
                        "Comment"	TEXT,\
                        CONSTRAINT CHK_Redoublant CHECK (Redoublant=\'Oui\' or Redoublant=\'Non\')\
                        )')
        self.db.commit()

    def get_list(self):
        db = sqlite3.connect(self.db_path)
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
        return L

    def supprimer(self, ID):
        self.db = sqlite3.connect(self.db_path)
        self.db.execute('DELETE FROM Marks\
            WHERE ID={}'.format(ID))
        self.db.commit()
    def modifier(self, ID, name, note, redoublant, appreciation):
        self.db = sqlite3.connect(self.db_path)
        self.db.execute('UPDATE Marks\
                        SET Nom = \"{}\", Note= {}, Redoublant = \"{}\", Comment = \"{}\" \
                        WHERE ID = \"{}\";'.format(name, note, redoublant, appreciation, ID))
        self.db.commit()
        self.db.close()