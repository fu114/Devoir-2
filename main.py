from Scripts.Interface.Interface import *
from Scripts.Commands.SQLrequests import *

def main():
    master = Tk()
    master.title('Application de gestion des notes')
    foo = Interface(master)
    master.mainloop()

if __name__ == '__main__':
    main()