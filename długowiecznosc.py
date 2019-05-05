# Długowieczność
# Demonstruje wigdety Text i Entry oraz menedżer układu Grid

from tkinter import *

class Apka(Frame):
    """Aplikacja z GUI, która może ujawnić sekret długowieczności"""
    def __init__(self, master):
        """Inicjalizuj ramkę"""
        super(Apka, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Utwórz widgety typu Button, Test i Entry"""
        # utwóz etykietę z instrukcją
        self.inst_lbl = Label(self, text = "Wprowadź hasło do sekretu długowieczności")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        # utwórz etykietę do hasła
        self.pw_lbl = Label(self, text = "Hasło: ")
        self.pw_lbl.grid(row = 1, column = 0, sticky = W)
        # utwórz widget Entry do przyjęcia hasła
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = W)
        # utwórz przycisk 'Akceptuj'
        self.submit_bttn = Button(self, text = 'Akceptuj', command = self.reveal)
        self.submit_bttn.grid(row = 2, column = 0, sticky = W)
        # utwórz widget typu Text
        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)

    def reveal(self):
        """Wyświetl komunikat zależny od poprawności hasła"""
        contents = self.pw_ent.get()
        if contents == 'sekret':
            message = "Oto tajemny przepis na dożycie 100 lat: dożyj 99 lat, a potem bądź BARDZO ostrożny."
        else:
            message = "To nie jest poprawne hasło, więc nie mogę się z Tobą podzielić swoim sekretem."
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)


# część główna
root = Tk()
root.title('Długowieczność')
root.geometry('300x150')

app = Apka(root)

root.mainloop()
