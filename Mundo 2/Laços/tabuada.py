numero = int(input("Digite um número: "))
#Dessa forma aqui teria que fazer vários IF's..
'''
for x in range(1, 10):
    if numero == 1:
        print("{} x {} = {}".format(numero, x, (x * numero)))
    elif numero == 2:
        print("{} x {} = {}".format(numero, x, (x * numero)))
'''
#Aqui já ficou mais simples e o código menor.
for x in range(1, 10):
    if numero == x:
        print("{} x {} = {}".format(numero, x, (x * numero)))
    else: print("{} x {} = {}".format(numero, x, (x * numero)))
