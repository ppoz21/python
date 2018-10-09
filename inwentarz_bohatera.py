#Inwentarz bohatera
#Demonstruje tworzenie krotek

#utwórz pustą krotkę
inventory = ()

#potraktuj krotkę jako warunek
if not inventory:
    print("Nie posiadasz niczego")

input("\nAle co to? Na strychu leży torba. Nsaciśnij Enter, aby zobaczyć co jest w środku")

#utwórz krotkę zawierającą pewne elementy
inventory = ("Miecz",
             "Zbroja",
             "Tarcza",
             "Napój uzdrawiający")

#wyświetl krotkę
print("\nSkrzynka zawiera:")
print(inventory)

#wyświetl poszczególne elementy krotki

print("\nElementy Twojego wyposażenia:")
for item in inventory:
    print(item)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")