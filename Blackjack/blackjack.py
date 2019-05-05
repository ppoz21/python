# Blackjack
# od 1 do 7 graczy współzawodniczy z rozdającym

import karty, gra

class BJ_Card(karty.Karta):
    """Karta do Blackjacka"""
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.KOLORY.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(karty.Talia):
    """Talia kart do Blackjacka"""
    def populacja(self):
        for kolor in BJ_Card.KOLORY:
            for karta in BJ_Card.KARTY:
                self.karty.append(BJ_Card(kolor, karta))

class BJ_Hand(karty.Reka):
    """Ręka w Blackjacku"""
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        #jeśli karta w ręce ma wartość None, to i wartość sumy wynosi None
        for karta in self.karty:
            if not karta.value:
                return None
        # zsumuj wartości kart, traktuj każdego asa jako 1
        t = 0
        for karta in self.karty:
             t += karta.value

        # ustal, czy ręka zawiera asa
        contain_ace = False
        for karta in self.karty:
            if karta.value == BJ_Card.ACE_VALUE:
                contain_ace = True

        # jeśli ręka zawiera asa, a suma jest wystarczająco niska, potraktuj asa jako 11

        if contain_ace and t <=11:
            # dodaj tylko 1, ponieważ dodaliśmy 1 za asa
            t += 10

        return t

    def is_busted(self):
        return self.total > 21

class BJ_Player(BJ_Hand):
    """Gracz w Blackjacku"""
    def is_hitting(self):
        response = gra.ask_yes_no("\n" + self.name + ", czy chcesz dobrać kartę? (T/N): ")
        return response

    def bust(self):
        print(self.name, "ma furę.")

    def lose(self):
        print(self.name, "przegrywa.")

    def win(self):
        print(self.name, "wygrywa.")

    def push(self):
        print(self.name, "remisuje.")

class BJ_Dealer(BJ_Hand):
    """Rozdający w Blackjacku"""
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "ma furę.")

    def flip_first_card(self):
        first_card = self.karty[0]
        first_card.flip()

class BJ_Game(object):
    """Gra w Blackjacka"""
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Rozdający")

        self.deck = BJ_Deck()
        self.deck.populacja()
        self.deck.tasuj()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.rozdaj([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        # rozdaj każdemu początkowe dwie karty
        self.deck.rozdaj(self.players + [self.dealer], na_reke = 2)
        self.dealer.flip_first_card()    #ukryj pierwszą kartę rozdającego
        for player in self.players:
            print(player)
        print(self.dealer)

        # rozdaj graczom dodatkowe karty
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()     #odsłoń pierwszą kartę  rozdającego

        if not self.still_playing:
            # ponieważ wszyscy gracze dostali furę, pokaż tylko rękę rozdającego
            print(self.dealer)
        else:
            # porównaj punkty każdego gracza pozostającego w grze z punktami rozdającego
            for player in self.still_playing:
                if player.total > self.dealer.total:
                    player.win()
                elif player.total < self.dealer.total:
                    player.lose()
                else:
                    player.push()
        #usuń karty wszystkich graczy
        for player in self.players:
            player.czysc()
        self.dealer.czysc()

def main():
    print("\t\tWitaj w grze 'Blackjack!\n")

    names = []
    number = gra.ask_number("Podaj liczbę graczy (1-7): ", low = 1, high = 8)
    for i in range(number):
        name = input("Wprowadź nazwę gracza: ")
        names.append(name)
    print()

    game = BJ_Game(names)

    again = None

    while again !="n":
        game.play()
        again = gra.ask_yes_no("\nCzy chcesz zagrać ponownie? (T/N): ")

main()
input("Aby zakończyć naciśnij Enter.")
