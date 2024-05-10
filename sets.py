lista =[1,1,2,3,3,1,4,8,3]

lista_unica=[]
# por elemento
for numero in lista:
    print(numero)

#por indice
for i in range(len(lista)):
    print(lista[i])

for numero in lista:
    if numero not in lista_unica:
        lista_unica.append(numero)

print(lista_unica)
lista_unica_2=set(lista)
print(lista_unica_2)
print(type(lista_unica_2))

grupo_1=set('abracadra')
grupo_2=set("alacazam")
print(grupo_1)
print(grupo_2)
print(grupo_2-grupo_1)
print(grupo_2&grupo_1)
print(grupo_2|grupo_1)
print(grupo_2^grupo_1)
print(grupo_2&grupo_1)|(grupo_2-grupo_1)