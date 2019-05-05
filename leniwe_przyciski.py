# Leniwe przyciski
# Demonstruje tworzenie przycisków

from tkinter import *

#utwórz okno główne
root = Tk()
root.title("Leniwe przyciski")
root.geometry("1280x720")

# utwórz w oknie ramkę do pomieszczenia innych widgetów
app = Frame(root)
app.grid()

# utwórzy w ramce przycisk
bttn1 = Button(app, text = "Nic nie robię!")
bttn1.grid()

# utwórzy w ramce drugi przycisk
bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text = "Ja również!")

# utwórzy w ramce trzeci przycisk
bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "To samo mnie dotyczy!"

# uruchom pętlę zdarzeń okna głównego
root.mainloop()
