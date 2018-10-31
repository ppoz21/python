#instrukcja
#demonstruje tworzenie funkcji

def instrukcja():
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

#main
print("Wywoływanie instrukcji: ")
instrukcja()
print("Ponowne wywołanie instrukcji: ")
instrukcja()
print("Prawdopodobnie teraz już zrozumiałeś tę grę.")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")