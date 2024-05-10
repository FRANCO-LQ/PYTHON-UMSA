'''crea un programa en un tablero-de-ajedrez'''
n, m = list(map(int, input("Dimensión: ").split()))
for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            print("#", end=' ')
        else:
            print("", end=' ')
    print(" ")