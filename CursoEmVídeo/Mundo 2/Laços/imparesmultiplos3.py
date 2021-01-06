valor = 0
for x in range(1, 500+1):
    if x % 2 != 0:
        if x % 3 == 0:
            valor +=x
print(valor)