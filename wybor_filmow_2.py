# Wybór filmów 2
# Demonstruje przycisk opcji

from tkinter import *

class Apka(Frame):
    """Aplikacja z  GUI służąca do wyboru ulubionego gatunku filmowego"""
    def __init__(self, master):
        """Inicjalizuj ramkę"""
        super(Apka, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Utwórz widgety umożliwiające wybór gatunku filmowego"""
        # utwórz etykietę z opisem
        Label(self, text = "Wybierz swó julubiony gatunek filmu").grid(row = 0, column = 0, sticky = W)

        # utwórz etykietę z instrukcją
        Label(self, text = "Wybierz jeden gatumnek:").grid(row = 1, column = 0, sticky = W)

        # utwórz zmienną, która ma reprezentowć pojedynczy, ulubiony gatunek filmu
        self.favourite = StringVar()
        self.favourite.set(None)

        # utwórz przycisk opcji do wyboru komedii
        Radiobutton(self, text = "komedia", variable = self.favourite, value = 'komedia', command = self.update_text).grid(row = 2, column = 0, sticky = W)

        # utwórz przycisk opcji do wyboru dramatu
        Radiobutton(self, text = "dramat", variable = self.favourite, value = 'dramat', command = self.update_text).grid(row = 3, column = 0, sticky = W)

        # utwórz przycisk opcji wyboru romansu
        Radiobutton(self, text = "romans", variable = self.favourite, value = 'romans', command = self.update_text).grid(row = 4, column = 0, sticky = W)

        # utwórz pole tekstowe do wyświetlania wyników
        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)

    def update_text(self):
        """Zaktualizuj pole tekstowe i wyświetl ulubiony gatunnek filmu użytkownika"""
        message = 'Twoim ulubionym gatunkiem filmu jest '
        message += self.favourite.get()
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)


# część główna
root = Tk()
root.title('Wybór filmów 2')
app = Apka(root)
root.mainloop()
