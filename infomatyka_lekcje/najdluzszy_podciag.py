def najdluzszy_podciag(ciag):
    n = len(ciag)
    x = 0
    max = 0
    for i in range(x, n):
        if i in ciag:
            max += 1
            x = i
            for i in range(x,n):
                if i in ciag:
                    max += 1
                    x = i
    return max


ciag = [1, 3, 2, 5, 3 , 6, 7, 4, 5, 8]
print(najdluzszy_podciag(ciag))
