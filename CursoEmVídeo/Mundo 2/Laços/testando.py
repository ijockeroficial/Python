'''
n = int(input("Digite um número: "))
for x in range(0, n+1):
    print(x)
print("Fim")
'''
'''
inicio = int(input("Digite um número: "))
final = int(input("Digite um número: "))
passo = int(input("Digite um número: "))
for x in range(inicio, final+1, passo):
    print(x)
print("Fim")
'''
s = 0
for x in range(0, 4):
    n = int(input("Digite um número: "))
    s += n
print("A soma dos números é: {}".format(s))