laco = [1,2,3,4,5]
for x in range(0, 5):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        laco[x] = numero
    else: print("Número Impar Desconsiderado!")
print(sum(laco))

#Correção:
'''
soma = 0
count = 0
for x in range(1, 7):
    num = int(input("Digite o {} número: ".format(x)))
    soma += num
    count += 1
print("Você informou {} números e a soma foi {}".format(count, soma))
'''
