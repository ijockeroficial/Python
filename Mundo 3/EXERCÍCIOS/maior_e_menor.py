#CORREÇÃO
listanum= []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input("Digite um número: ")))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print(f"O maior valor digitado foi: {mai}")
print(f"O menor valor digitado foi: {men}")

'''
x=1
lista = []
while x <= 5:
    numero = input("Digite um número:")
    lista += numero
    x += 1
z = 0
while z < 4:
    if lista[z] < lista[z+1]:
        maior = lista[z]
    x += 1
print(maior)
'''