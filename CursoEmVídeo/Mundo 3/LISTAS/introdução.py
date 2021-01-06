'''
    LISTAS É DIFERENTE DE TUPLAS.
    Tuplas utiliza-se: ()
    Listas utiliza-se: []
'''
#TUPLA:
verduras = ("cenoura", "beterraba", "alface", "chuchu")
#LISTAS:
verduras2 = ["cenoura", "beterraba", "alface", "chuchu"]
'''-------------------------------------------------------'''
#Exemplos.:
print(verduras)
print(verduras2[3])
'''
    Não da pra fazer isso com tuplas.
    tipo: verduras(3) = "Arroz"   
'''
verduras2[3] = "Macarrao"
print(verduras2)
print(verduras2[3])

