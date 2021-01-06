lista = list()
while True:
    continuar = str(input("Quer continuar? S ou N ")).upper()
    if continuar == "S":
        lista.append(int(input("Digite um número: ")))
    else: 
        if continuar == "N":
            break
print(f"Foram digitados: {len(lista)} números")
lista.sort(reverse = True)
print(lista)
if 5 in lista:
    print("O valor 5 foi digitado e está na lista!")
else: print("O valor 5 não foi digitado!")