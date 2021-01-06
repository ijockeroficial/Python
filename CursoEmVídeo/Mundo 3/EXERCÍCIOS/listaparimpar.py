lista = []
while True:
    continuar = str(input("Quer continuar ? S ou N ")).upper()
    if continuar == "S":
        lista.append(int(input("Digite um número: ")))
    else:
        if continuar == "N":
            break

par = []
impar = []
for x in range(0, len(lista)):
    if lista[x] % 2 == 0:
        par.append(lista[x])
    else:
        if lista[x] % 2 == 1:
            impar.append(lista[x])
    x += 1
print(f"Os numeros da lista são: {lista}")
print(f"Os numeros pares sao: {par}")
print(f"Os numeros impares sao: {impar}")
