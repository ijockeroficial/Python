#LISTA
verduras2 = ["cenoura", "beterraba", "alface", "chuchu"]
print("Mostrando os elementos da lista")
print(verduras2)
print('-' * 50)
#Tem como remover elementos de uma lista usando: pop(), remove() e del.
#Usando o DEL
print("Comando DEL")
del verduras2[2]
print(verduras2)
print('-' * 50)
#Usando o POP()
print("Método POP()")
verduras2.pop(1)
print(verduras2)
print('-' * 50)
#Usando o REMOVE()
print("Método REMOVE()")
verduras2.remove("cenoura")
print(verduras2)
print('-' * 50)