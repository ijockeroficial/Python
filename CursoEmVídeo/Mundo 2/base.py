numero = int(input("Digite um número inteiro: "))
print("#" * 20)
print("Bases de conversão")
print("1 - para binário")
print("2 - para octal")
print("3 - para hexadecimal")
print("#" * 20)
base = int(input("Escolha a base de conversão: "))

if base == 1:
    print("Escolheu a base 1")
elif base == 2:
    print("Escolheu a base 2")
elif base == 3:
    print("Escolheu a base 3")
else: print("Essa base não existe nas opções acima!")