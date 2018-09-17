# Sprzedawca samochodów
# konwersja wprowadzonej ceny poprzzez dodanie podatków, prowizji, opłat

auto = int(input("Wprowadź cenę samochodu:"))

podatek = auto * 0.23

o_rej = 180

prowizja = auto * 0.05

dostarczenie = 200

cena_koncowa = auto + podatek + o_rej + prowizja + dostarczenie

print("Podatek VAT wynosi: ", podatek)
print("Prowizja wynosi: ", prowizja)


print("Całkowity koszt sprzedaży samochodu (włącznie ze wszystkimi opłatami wynosi: ", cena_koncowa)

input("Naciśnij Enter, aby zakończyć działanie programu")
