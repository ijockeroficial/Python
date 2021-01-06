#Correção
lista = []
Continuar = True
while Continuar:
    numero = int(input("Digite um número: "))
    parar = str(input("Quer parar? S ou N ")).upper()
    if numero not in lista:
        lista.append(numero)
    if parar == "S":
        Continuar = False
    else:
        if parar == "N":
            Continuar = True
lista.sort()
print(lista)

'''
#Tentativa 3 CERTO
listanum = []
x = 0
valor = True
while valor:
    listanum.append(int(input("Digite um número: ")))
    resposta = str(input("Quer continuar? Digite: S ")).upper()
    if resposta == "S":
        valor = True
    else: valor = False

final = set(listanum)


7

[4,5,6,7]

5,6,7,8

print(final)
'''

'''
#Tentativa 2
listanum = []
x = 0
valor = True
while valor:
    listanum.append(int(input("Digite um número: ")))
    resposta = str(input("Quer continuar? Digite: S ")).upper()
    if resposta == "S":
        valor = True
    else: valor = False

for x, y in enumerate(listanum):
    if y == y and x != x-1:
        listanum.remove(y)

print(listanum)
'''



'''
#Primeira Tentativa de fazer
listanum = []
x = 01
valor = True
while valor:
    listanum.append(int(input("Digite um número: ")))
    if x != 0:
        if listanum[x] != listanum[x - 1]:
            valor = True
        else: listanum.pop(x)
    else:
        continuar = str(input("Quer continuar ? S ou N")).upper()
        if continuar == "S":
            valor = True
        else: 
            if continuar == "N":
                valor = False
    x += 1
print(listanum)
'''

