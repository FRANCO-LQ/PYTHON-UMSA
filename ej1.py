from typing import List, Any

animales = ['perro', 'gato', 'Tigre,'' Alcon']
for animal in animales:
    print(animal)
    break
for i in range(len(animales)):
    print(range(int(i)))
    break
for i in range(len(animales)):
    print(f'(i).- (animales[i])')
    break
print(range(10))
print(range(5, 10))
print(range(5, 10))
print(range(2, 10, 2))
for i in range(5, 10):
    print(i)
print('================')
for i in range(2, 10, 2):
    print(i)
    break
potencias = [x ** 2 for x in range(1, 11)]
print(potencias)

lista = []
for x in range(1, 11):
    lista.append(x ** 2)
print(lista)
print("---------------------------")
edades= [14,23,17,89,5,56,2]
for edad in edades:
    if edad >= 18 or edad <= 60:
        print(f'{edad} es Adulto:')
        break
    elif edad > 17 or edad <= 12:
        print(f"{edad} es adolescente")
        break
    elif edad > 5 or edad <= 11:
        print(f"{edad} es niño")
        break
    elif edad > 0 or edad <= 5:
        print(f"{edad} infante")
        break
    elif edad > 60:
        print(f'{edad} Es anciano')
