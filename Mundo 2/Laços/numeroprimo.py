numero = int(input("Digite um número: "))
total = 0
for x in range(1, numero + 1):
    if numero % x == 0:
        print("\033[33m", end=' ')
        total += 1
    else: print("\033[34m", end=' ')
    print('{} '.format(x), end=' ')
print("\n\033[mO número {} foi divisivel {} vezes".format(numero, total))
if total == 2:
    print("E por isso ele é PRIMO!")
else: print("E por isso ele não é PRIMO!")