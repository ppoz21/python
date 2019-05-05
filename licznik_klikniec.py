# Licznik kliknięć
# Demonstruje powiązanie zdarzenia z procedurą obsługi zdarzeń

from tkinter import *

class Apka(Frame):
    """Aplikacja z GUI, która zlicza kliknięcia przycisku"""
    def __init__(self, master):
        """Inicjalizuj ramkę"""
        super(Apka, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0 # liczba kliknięć przycisku
        self.create_widgets()

    def create_widgets(self):
        """Utwórz przycisk, który wyświetla liczbę kliknięć"""
        self.bttn = Button(self)
        self.bttn['text'] = "Liczba kliknięć: 0"
        self.bttn['command'] = self.update_count
        self.bttn.grid()

    def update_count(self):
        """Zwiększ licznik kliknięć i wyświetl jego nową wartość"""
        self.bttn_clicks += 1
        self.bttn['text'] = "Liczba kliknięć: " + str(self.bttn_clicks)


# część główna
root = Tk()
root.title('licznik kliknięć')
root.geometry("200x50")

app = Apka(root)

root.mainloop()
