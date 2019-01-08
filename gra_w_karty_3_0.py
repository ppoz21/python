# Gra w karty 3.0
# Demonstruje dziedziczenie - przesłanianie metod

class Karta(object):
    """Karta do gry"""
    KARTY = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    KOLORY = ["♥", "♠", "♦", "♣"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Niewyświetlalna_Karta(Karta):
    """Karta, której ranga i kolor nie są ujawniane przy jej wyświetleniu"""
    def __str__(self):
        return "<utajniona>"

class Zmienialna(Karta):
    """Karta może nbyć odkryta lub zakryta"""
    def __init__(self, rank, suit, face_up = True):
        super(Zmienialna, self).__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super(Zmienialna, self).__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


# main
karta1 = Karta(rank="A", suit="♣")
karta2 = Niewyświetlalna_Karta(rank="Q", suit="♠")
karta3 = Zmienialna(rank="K", suit="♥")

print("Wyświetlanie obiektu klasy Karta:")
print(karta1)
print("Wyświetlanie obiektu klasy Niewyświetlalna_Karta:")
print(karta2)
print("Wyświetlanie obiektu klasy Zmienialna:")
print(karta3)

print("Odwrócenie stanu obiektu klasy Zmienialna (odkrycie-zakrycie karty).")
karta3.flip()

print("Wyświetlanie obiektu klasy Zmienialna:")
print(karta3)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
