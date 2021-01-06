#Programa que mostra os dígitos separados.
numero = int(input("Digite um número entre 0 e 9999: "))
#Correção
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))

#Fiz assim.
numero = str(numero)
print(" ".join(numero))
numero2 = " ".join(numero).split()
for x in numero2:
    print(x) 