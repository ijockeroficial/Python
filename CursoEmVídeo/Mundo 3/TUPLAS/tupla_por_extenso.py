tupla = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez")
nu = (0,1,2,3,4,5,6,7,8,9,10)

numero = int(input("Digite um número: "))

if numero in nu:
    print("Seu número por extenso é: {}".format(tupla[numero]))
else: print("Esse número não tem na tupla. ;(")

#Correção:
'''
cont = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez")
while True:
    numero = int(input("Digite um número: "))
    if 0 <= numero <= 10:
        break
    print("Tente novamente. ", end=' ')
print("Você digitou o número {cont[numero]}")
'''