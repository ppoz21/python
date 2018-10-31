# Kółko i krzyżyk
# Komputer gra w kółko i krzyżyk przeciwko człowiekowi

# stałe globalne
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


def wyswietl_instrukcje():
    """Wyświetl instrukcję gry"""
    print(
        """
        Witaj w największym intelektualnym wyzwaniu wszech czasów, jakim jest
        gra 'Kółko i krzyżyk'. Będzie to ostateczna rozgrywka między Twoim
        ludzkim mózgiem a moim krzemowym procesorem.
        Swoje posunięcie wskażesz poprzez wprowadzenie liczby z zakresu 0 - 8.
        Liczba ta odpowiada pozycji na planszy zgodnie z poniższym schematem:
                                        0 | 1 | 2
                                        ---------
                                        3 | 4 | 5
                                        ---------
                                        6 | 7 | 8
        Przygotuj się, Człowieku. Ostateczna batalia niebawem się rozpocznie. \n
        """
    )


def tak_nie(pytanie):
    """Zadaje pytanie i oczekuje odpowiedzi tak lub nie"""
    response = None
    while response not in ("t","n"):
        response = input(pytanie).lower()
    return response


def liczba_z_zakresu(pytanie, poczatek, koniec):
    """Poproś o podanie liczby z odpowiedniego zakresu"""
    response = None
    while response not in range(poczatek, koniec):
        response = int(input(pytanie))
    return response


def kto_zaczyna():
    """Ustal, czy pierwszy ruch należy do gracza, czy do komputera"""
    go_first = tak_nie("Czy chcesz mieć prawo do pierwszego ruchu? (t/n): ")
    if go_first == "t":
        print("\nWięc pierwszy ruch należy do Ciebie. Będzie Ci potrzebny.")
        human = X
        computer = O
    else:
        print("\nTwoja odwaga Cię zgubi... Ja wykonuję pierwszy ruch.")
        computer = X
        human = O
    return computer, human


def nowa_plansza():
    """Utwórz nową planszę gry"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def wyswietl_plansze(board):
    """Wyświetl plansze gry na ekranie"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def dostepne_ruchy(board):
    """Utwórz listę prawodlowych ruchów"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def zwyciezca(board):
    """Ustal zwycizce gry"""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None


def ruch_gracza(board, human):
    """Odczytaj ruch gracza"""
    legal = dostepne_ruchy(board)
    move = None
    while move not in legal:
        move = liczba_z_zakresu("Jaki będzie Twój ruch? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nTo pole jest już zajęte, niemądry Człowieku. Wybierz inne.\n")
    print("Znakomicie...")
    return move


def ruch_komputera(board, computer, human):
    """Spowoduje wykonanie ruchu przez komputer"""
    #utwórz kopię roboczą, ponieważ funkcja będzie zmieniać listę
    board = board[:]

    #najlepsze pozycje do zajęcia według kolejności
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Wybieram pole numer", end=" ")

    #jeśli komputer może wygrać, wykonaj ten ruch
    for move in dostepne_ruchy(board):
        board[move] = computer
        if zwyciezca(board) == computer:
            print(move)
            return move
        #ten ruch został sprawdzony, wycofaj go
        board[move] = EMPTY

    #jeśli człowiek może wygrać, zablokuj ten ruch
    for move in dostepne_ruchy(board):
        board[move] = human
        if zwyciezca(board) == human:
            print(move)
            return move
        #ten ruch został sprawdzony, wycofaj go
        board[move] = EMPTY

    #ponieważ nikt nie może wygrać w następnym ruchu, wybierz najlepsze wolne pole
    for move in BEST_MOVES:
        if move in dostepne_ruchy(board):
            print(move)
            return move


def nastepny_ruch(turn):
    """Zmień wykonawcę ruchu"""
    if turn == X:
        return O
    else:
        return X


def gratulacje_zwyciezcy(the_winner, computer, human):
    """Pogratuluj zwycięzcy"""
    if the_winner != TIE:
        print(the_winner, "jest zwycięzcą!\n")
    else:
        print("Remis!\n")

    if the_winner == computer:
        print("Jak przewidywałem, Człowieku, jeszcze raz zostałem triumfatorem. \n" \
              "Dowód na to, że komputery przewyższają ludzi pod każdym względem.")

    elif the_winner == human:
        print("No nie! To niemożliwe! Jakoś udało Ci się mnie zwieść, Człowieku. \n" \
              "Ale to się nigdy nie powtórzy! Ja, komputer, przyrzekam Ci to!")

    elif the_winner == TIE:
        print("Miałeś mnóstwo szczęścia, Człowieku, i jakoś udało Ci się ze mną " \
              "zremisować. \nŚwiętuj ten dzień... bo to najlepszy wynik, jaki możesz " \
              "kiedykolwiek osiągnąć.")


def main():
    wyswietl_instrukcje()
    computer, human = kto_zaczyna()
    turn = X
    board = nowa_plansza()
    wyswietl_plansze(board)

    while not zwyciezca(board):
        if turn == human:
            move = ruch_gracza(board, human)
            board[move] = human
        else:
            move = ruch_komputera(board, computer, human)
            board[move] = computer
        wyswietl_plansze(board)
        turn = nastepny_ruch(turn)

    the_winner = zwyciezca(board)
    gratulacje_zwyciezcy(the_winner, computer, human)


#rozpocznij program
main()
input("\n\nAby zakończyć grę, naciśnij klawisz Enter.")