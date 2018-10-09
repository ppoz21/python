#wymieszane litery
#komputer wybiera słowo, a potem miesza w nim litery
#gracz powinien odgadnąć pierwotne słowo

import random

#utwórz sekwencję słów do wyboru (kiedyś zaimportuje tu plik ze słowami xD)
WORDS = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")

#wybierz losowo słowo z sekwencji
word = random.choice(WORDS)

#utwórz zmienną, by późnij sprawdzić czy odpowiedź jest porawna
correct = word

#utwórz pomieszaną wersję słowa
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# rozpocznij grę
print(
"""
            Witaj w grze 'Wymieszane litery'!
    Uporządkuj litery, aby odtworzyć prawidłowe słowo.
(Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
"""
)
print("Zgadnij, jakie to słowo:", jumble)

guess = input("\nTwoja odpowiedź: ")
while guess !=correct and guess !="":
    print("Niestety, to nie to slowo")
    guess = input("Twoja odpowiedź: ")

if guess == correct:
    print("Zgadza się! Zgadłeś\n")

print("Dziękuję za udział w grze.")

input("\n\nAby zakończyc program, naciśnij klawisz Enter.")