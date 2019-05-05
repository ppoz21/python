# Przelicznik binarny
# Przelicza liczby z systemu binarnego na dziesiętny i odwrotnie

from tkinter import *


class Przelicznik(Frame):
    def __init__(self, master):
        super(Przelicznik, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        Label(self,
              text="Przelicznik pozycyjno-wagowy"
              ).grid(row = 0, sticky = W)
        Label(self,
              text="Wybierz tryb działania Przelicznika: "
              ).grid(row = 1, column = 0, sticky = W)
        self.tryb = StringVar()
        self.tryb.set(None)
        Radiobutton(self,
                    text = "dzisiętno-binarny",
                    variable = self.tryb,
                    value = 'dec-bin'
                    ).grid(row = 2, column = 0, sticky = W)
        Radiobutton(self,
                    text="binarno-dziesiętny",
                    variable=self.tryb,
                    value='bin-dec'
                    ).grid(row=2, column=1, sticky=W)
        Label(self,
              text = "Liczba do przeliczenia: "
              ).grid(row = 4, column = 0, sticky = W)
        self.int_ent = Entry(self)
        self.int_ent.grid(row = 4, column = 1, sticky = W)
        Button(self,
               text = "Przelicz",
               command = self.wybierz_funkcje,
               ).grid(row = 6, column = 0, sticky = W)
        Label(self,
              text="Liczba po przeliczeniu: "
              ).grid(row=8, column=0, sticky=W)
        self.wynik = Text(self, width=15, height = 1, wrap = WORD)
        self.wynik.grid(row=8, column=1,sticky=W)

    def wybierz_funkcje(self):
        tryb = self.tryb.get()
        liczba = int(self.int_ent.get())
        if tryb == 'dec-bin':
            self.dec_to_bin(liczba)

        elif tryb == 'bin-dec':
            self.bin_to_dec(liczba)

    def dec_to_bin(self, liczba):
        self.wynik.delete(0.0, END)
        self.wynik.insert(0.0, int(bin(liczba)[2:]))

    def bin_to_dec(self, liczba):
        self.wynik.delete(0.0, END)
        self.wynik.insert(0.0, int(str(liczba), 2))


# część główna
root = Tk()
root.title("Przelicznik pozycyjno-wagowy")
app = Przelicznik(root)
root.mainloop()