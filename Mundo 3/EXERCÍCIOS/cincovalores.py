#CORREÇÃO
lista = list()
for x in range(0, 5):
    numero = int(input("Digite um número: "))
    if x == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                break
            pos += 1
print(lista)

'''
#Primeira tentativa
lista = list()
x = 0
while x <= 4:
    numero = input("Digite um número: ")
    if x == 0:
        lista += numero
    else:
        #Se o valor da posição anterior for maior que o valor do número
        if lista[x - 1] > numero:
            lista[x] += lista[x - 1]
            lista[x - 1] += numero
        else:
            lista += numero
    x += 1
print(lista)
'''
