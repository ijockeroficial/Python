#CORREÇÃO
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #Cria 3 Listas dentro de uma lista.
spar = mai = scol = 0
#Coleta os valores digitados e salva na lista: matriz
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para as posiçoes [{l},{c}]: "))
#O print cria uma linha para melhorar a aparencia  
print("_" * 50)
#Faz a matriz 3x3 com os números da lista: matriz.
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end=" ") #Esse comando: :^5 faz com que fique em 5 espaços e centraliza o numero.
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print() #Esse print é pra pular uma linha
#O print cria uma linha para melhorar a aparencia  
print("_" * 50)
print(f"A soma de todos os valores pares são: {spar}")
for l in range(0, 3):
    scol += matriz[l][2]
print(f"A soma dos números da 3º coluna é: {scol}")
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]

print(f"O maior valor da 2 linha é: {mai}")

'''
#Fiz assim:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #Cria 3 Listas dentro de uma lista.
par = 0
impar = 0
#Coleta os valores digitados e salva na lista: matriz
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para as posiçoes [{l},{c}]: "))
#O print cria uma linha para melhorar a aparencia  
print("_" * 50)
#Faz a matriz 3x3 com os números da lista: matriz.
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end=" ") #Esse comando: :^5 faz com que fique em 5 espaços e centraliza o numero.
    print() #Esse print é pra pular uma linha
#O print cria uma linha para melhorar a aparencia  
print("_" * 50)

#Esse for percorre a lista "matriz" e soma todos os números pares e impares.
#Faz a soma dos números da 3 coluna.
#Verifica qual o número maior da 2º linha da matriz gerada pelo for anterior.

soma3ºcoluna = 0
for x, y in enumerate(matriz):
    if y[0] % 2 == 0:
        par += y[0]
    else:
        impar += y[0]
    if y[1] % 2 == 0:
        par += y[1]
    else:
        impar += y[1]
    if y[2] % 2 == 0:
        par += y[2]
    else:
        impar += y[2]
    soma3ºcoluna += y[2]
    if x == 1:
        if y[0] > y[1] and y[2] < y[1]:
            soma2ºcoluna = y[0]
        else:
            if y[1] > y[0] and y[2] < y[0]:
                soma2ºcoluna = y[1]
            else: 
                if y[2] > y[1] and y[0] < y[1]:
                    soma2ºcoluna = y[2]
print(f"A soma de todos os valores pares são: {par}")
print(f"A soma de todos os valores ímpares são: {impar}")
print(f"A soma dos números da 3º coluna é: {soma3ºcoluna}")
print(f"O maior valor da 2 linha é: {soma2ºcoluna}")
'''