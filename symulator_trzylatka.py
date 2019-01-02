#Symulator trzylatka
#Demonstruje pentlę while

print("\tWitaj w 'Symulatorze trzylatka'\n")
print("Ten program symuluje rozmowę z trzyletnim dzieckiem.")
print("Spróbuj przerwać to szaleństwo.\n")

response = ""
while response != "bo tak temu".lower():
    response = input("Czemu?\n").lower()
print("Powiem mamie!")
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")