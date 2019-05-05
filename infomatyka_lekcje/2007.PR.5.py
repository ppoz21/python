# superpierwsza


def is_prime(liczba):
    import math
    if liczba == 1:
        return False
    for i in range(2, int(math.sqrt(liczba)+1)):
        if liczba % i == 0:
            return False
    return True


def is_super_prime(liczba):
    cyfry = list(str(liczba))
    sum = 0
    for i in range(len(cyfry)):
        sum = sum + int(cyfry[i])
    if is_prime(sum):
        return True
    return False


def dec_to_bin(x):
    return int(bin(x)[2:])


def is_super_B_prime(liczba):
    binary = dec_to_bin(liczba)
    if is_super_prime(binary):
        return True
    return False


ile_w_2_do_1000 = 0
ile_w_100_do_10000 = 0
ile_w_1000_do_100000 = 0
z1 = open("1.txt", "w")
z2 = open("2.txt", "w")
z3 = open("3.txt", "w")
for i in range(2, 1001):
    if is_prime(i):
        if is_super_prime(i):
            if is_super_B_prime(i):
                ile_w_2_do_1000 += 1
                z1.write(str(i) + "\n")
z1.close()
print("Liczb super B pierwszych <2-1000>: ", ile_w_2_do_1000)
for i in range(100, 10001):
    if is_prime(i):
        if is_super_prime(i):
            if is_super_B_prime(i):
                ile_w_100_do_10000 += 1
                z2.write(str(i) + "\n")
z2.close()
print("Liczb super B pierwszych <100-10000>: ", ile_w_100_do_10000)
for i in range(1000, 100001):
    if is_prime(i):
        if is_super_prime(i):
            if is_super_B_prime(i):
                ile_w_1000_do_100000 += 1
                z3.write(str(i) + "\n")
z3.close()
print("Liczb super B pierwszych <1000-100000>: ", ile_w_1000_do_100000)

# b1)
ile_sum_100_1000 = 0
for i in range(100, 10001):
    if is_super_prime(i):
        ile_sum_100_1000 += 1

print("Ile jest liczb w przedziale <100,10000>, których suma cyfr jest liczbą pierwszą", ile_sum_100_1000)

# b2)
b2 = []
plik = open("2.txt", "r")
for linia in plik:
    b2.append(int(linia))
suma = sum(b2)
if is_prime(suma):
    print(suma, "to liczba pierwsza")
else:
    print(suma, 'to nie jest liczba pierwsza')
