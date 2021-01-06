x = 1
tupla = []
count = 0
par = []
'''
while x < 5:
    numero = int(input("Digite um número: "))
   
    x +=1
'''
for x in range(1, 5):
    numero = int(input("Digite um número: "))
    if numero == 9:
        count += 1
    if numero % 2 == 0:
        par += [numero]
    tupla += [numero]
print("Apareceu o valor 9: {} vezes".format(count))
if 3 in tupla:
    print("O valor 3 foi digitado na posição: {}".format(tupla.index(3)+1))
else: print("Não tem valor 3 nessa tupla!")
print("Os números pares foram: {}".format(par))

#Correção:
'''
numero = (
    int(input("Digite um número: ")),
    int(input("Digite um número: ")),
    int(input("Digite um número: ")),
    int(input("Digite um número: ")),
    int(input("Digite um número: ")))

print(f"Você digitou os valores {numero}")
print("O valor 9 apareceu {} vezes".format(numero.count(9)))
if 3 in tupla:
    print("O valor 3 foi digitado na posição: {}".format(tupla.index(3)+1))
else: print("Não tem valor 3 nessa tupla!")
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')
'''