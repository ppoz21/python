# Odczyatj to
# Demonstruje odczytywanie danych z pliku tekstowego

print("Otwarcie i zamknięcie pliku.")
text_file = open("odczytaj_to.txt", "r")
text_file.close()

print("\nOdczytywanie znaków z pliku.")
text_file = open("odczytaj_to.txt", "r")
print(text_file.read(1))
print(text_file.read(7))
text_file.close()

print("Odczytanie całego pliku zajednym razem.")
text_file = open("odczytaj_to.txt", "r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()

print("\nOdczytywanie po jednym wierszu na raz.")
text_file = open("odczytaj_to.txt", "r")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

print("Odczytywanie całego pliku do listy.")
text_file = open("odczytaj_to.txt", "r")
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()

print("\nPobieranie zawartości pliku wiersz po wierszu przy użyciu pętli.")
text_file = open("odczytaj_to.txt", "r")
for line in text_file:
    print(line)
text_file.close()

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
