numero = int(input("Informe um número inteiro: "))
x = numero
fatorial = 1
while x > 0:
    fatorial *= x
    x -= 1
print(fatorial)