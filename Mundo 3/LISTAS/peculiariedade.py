lista1 = [2, 5, 6, 7, 8]
#A lista 1 e a 2 são as mesma agora. Tudo que alterar na lista2, altera na lista1
lista2 = lista1
print(lista1)
print("_" * 50)
print(lista2)
print("_" * 50)
#Quando alterar uma das listas, altera nas duas.
#Adicionando o número 23 ao final da lista2.
lista2.append(23)
print(lista2)
print("_" * 50)
#A lista1 recebeu também a mesma alteração
print(lista1)
