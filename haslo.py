#Hasło
#Demonstruje instrukcję if oraz else

print("Witaj w systemie firmy Bezpieczny Komputer SA")
print("-- bezpieczeństwo to podstawa naszego działania\n")

password = input("Wprowadź hasło: ")

if password == "sekret":
    print("Dostęp został udzielony")
    print("Witaj! Musisz być kimś bardzo ważnym")
else:
    print("Odmowa dostępu")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")