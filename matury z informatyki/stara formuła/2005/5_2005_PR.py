# Zadanie 5
# Matura PR 2005
# Najlepsze sumy, najpopularniejsze elementy
def readFile(file):
    file = open(file, 'r')
    list = []
    for line in file:
        list.append(int(line))
    file.close()
    return list


def bestSum(list):
    n = len(list)
    s = list[0]
    sn = 0
    for i in range(0, n):
        for j in range(0, n):
            s += list[j]
            if s > sn:
                sn = s
            j += 1
        i += 1
    return sn


def mostPopular(list):
    counter = 0
    num = list[0]

    for i in list:
        curr_frequency = list.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i
    return num


list5_1 = readFile('dane\dane5-1.txt')
list5_2 = readFile('dane\dane5-2.txt')
list5_3 = readFile('dane\dane5-3.txt')

bestSum5_1 = bestSum(list5_1)
mostPopular5_1 = mostPopular(list5_1)
print(bestSum5_1)
print(mostPopular5_1)

bestSum5_2 = bestSum(list5_2)
mostPopular5_2 = mostPopular(list5_2)
print(bestSum5_2)
print(mostPopular5_2)

bestSum5_3 = bestSum(list5_3)
mostPopular5_3 = mostPopular(list5_3)
print(bestSum5_3)
print(mostPopular5_3)