# Metkownica
# Demonstruje etykietę

from tkinter import *

# utwórz okno główne
root = Tk()
root.title("Metkownica")
root.geometry("1280x720")

# utwórz w oknie ramkę, jako pojemnik na inne widgety
app = Frame(root)
app.grid()

# utwórz w ramce etykietę
lbl = Label(app, text = "Jestem etykietą!")
lbl.grid()

# uruchom pętlę zdarzeń okna
root.mainloop()