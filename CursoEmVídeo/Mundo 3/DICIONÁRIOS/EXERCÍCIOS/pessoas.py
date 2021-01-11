pessoas = {}
lista = []
mulheres = []
valor = True
cont = 0
média_idade = 0
while valor:
    cont += 1
    pessoas["nome"] = str(input("Nome: "))
    pessoas["sexo"] = str(input("Sexo: M/F ")).strip().upper()[0]
    pessoas["idade"] = int(input("Idade: "))
    média_idade += pessoas["idade"]
    if pessoas["sexo"] == "F":
        mulheres.append(pessoas["nome"])
    lista.append(pessoas.copy())
    continuar = str(input("Deseja continuar? S/N ")).strip().upper()[0]
    if continuar == "S":
        valor = True
        pessoas.clear()
    else: 
        if continuar == "N":
            valor = False
média = média_idade / cont
print("_" * 50)
print(f" - {cont} - pessoas foram cadastradas.")
print("_" * 50)
print(f"A média de idade é {média}")
print("_" * 50)
print("Lista de mulheres cadastradas: ")
print(mulheres)
acima = []
for x in lista:
    if x["idade"] > média:
        acima.append(x["nome"])
print("_" * 50)
print("Lista das pessoas com idade acima da média: ")
print(acima)
