#CORREÇÃO
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para as posiçoes [{l},{c}]: "))
print("_" * 50)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end=" ") #Esse comando: :^5 faz com que fique em 5 espaços centralizado.
    print()


'''
lista = []
valor = 1
while valor <= 9:
    lista.append(int(input("Digite um número: ")))
    valor += 1

for x in range(0, 3):
    print(f"[ {lista[x]} ] [ {lista[x + 1]} ] [ {lista[x + 2]} ]")
'''