#Tem como colocar uma lista dentro de outra
teste = list()
teste.append("Gustavo")
teste.append(40)
galera = list()
'''
galera.append(teste) <-- Adiciona a lista dentro da outra.
Só que com isso o que for alterado em uma altera na outra.
'''
galera.append(teste[:])  #Faz uma cópia da lista "teste".
teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:])
print(galera)
