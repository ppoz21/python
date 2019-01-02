# Zweirzak z konstruktorem
# demonstruje konstruktory


class Critter(object):
    """Wirtualny pupil"""
    def __init__(self):
        print("Urodził się nowy zwierzak!")

    def talk(self):
        print("CZeść! Jestem nowym obiektem klasy Critter")


# Część główna
crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")