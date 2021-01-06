lista = [[], []]
for x in range(1, 8):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        lista[0].append(numero) #Pega a lista que ta dentro da lista na posição 0  e adiciona o número;
    else:
        if numero % 2 != 0:
            lista[1].append(numero) #Pega a lista que ta dentro da lista na posição 1 e adiciona o número;
lista[0].sort()
print(lista[0])
lista[1].sort()
print(lista[1])