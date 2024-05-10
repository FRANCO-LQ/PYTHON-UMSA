# Pedir al usuario un número entero mayor a 0
while True:
    numero = int(input("Introduce un número entero: "))
    if numero > 0:
        break
    else:
        print("El número ingresado no es válido. Por favor, intenta de nuevo.")

# Mostrar la cuenta hacia atrás desde el número hasta 0
for i in range(numero, -1, -1):
    print(i, end=', ')
