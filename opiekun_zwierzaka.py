# Opiekun zwierzaka
# Wirtualny pupil, którym należy się opiekować

class Zwierzak(object):
    """Wirtualny pupil"""
    def __init__(self, name, glod = 0, nuda = 0):
        self.name = name
        self.glod = glod
        self.nuda = nuda

    def __uplyw_czasu(self):
        self.glod +=1
        self.nuda +=1

    @property
    def humor(self):
        niezadowolenie = self.glod + self.nuda
        if niezadowolenie <= 5:
            w = 'szczęśliwy'
        elif 5 <= niezadowolenie <= 10:
            w = 'zadowolony'
        elif 11 <= niezadowolenie <= 15:
            w = 'podenerwowany'
        else:
            w = 'wściekły'

        return w

    def mow(self):
        print('Nazywam się', self.name, 'i jestem', self.humor,'\n')
        self.__uplyw_czasu()

    def jedz(self, jedzenie = 4):
        print("Mniam, mniaj. Dziękuję.")
        self.glod -= jedzenie
        if self.glod < 0:
            self.glod= 0
        self.__uplyw_czasu()

    def baw_sie(self, zabawa = 4):
        print("Hurra!")
        self.nuda -= zabawa
        if self.nuda < 0:
            self.nuda = 0
        self.__uplyw_czasu()

def main():
    imie_zwierzaka = input("Jak chcesz nazwać swojego zwierzaka?: ")
    zwierzak = Zwierzak(imie_zwierzaka)
    wybor = None
    while wybor != "0":
        print \
        ("""
        Opiekun zwierzaka
        0 - zakończ
        1 - słuchaj swojego zwierzaka
        2 - nakarm swojego zwierzaka
        3 - pobaw się ze swoim zwierzakiem
        """)

        wybor = input("Wybierasz: ")
        print()

        # wyjdź z pętli
        if wybor == "0":
            print("Do widzenia")

        # słuchaj swojego zwierzaka
        elif wybor == "1":
            zwierzak.mow()

        # nakarm zwierzaka
        elif wybor == "2":
            zwierzak.jedz()

        #pobaw się
        elif wybor == "3":
            zwierzak.baw_sie()

        #nieznany wybór
        else:
            print("\n Niestety,", wybor, "nie jest prawidłowym wyborem")

main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")