#Fazer uma lista
'''
numeros = list(range(4, 11))
print(numeros)
nomes = ["Rogi", "Thiago", "Maria", "Carlos"]
print(nomes)
'''
#-------------------------------------------------
#Alterar a ordem da lista:
numeros2 = ["2", "4", "1", "3", "5"]
print(numeros2)
print("_" * 50)
#A função sort() ordena a lista de números em ordem crescente.
numeros2.sort()
print(numeros2)
print("_" * 50)
#A função sort(reverse=True) ordena a lista de números em ordem decrescente.
numeros2.sort(reverse=True)
print(numeros2)
print("_" * 50)
#Contar a quantidade de posições em uma lista usando o len()
print(len(numeros2))
