from datetime import datetime
pessoa = {}
pessoa["Nome"] = str(input("Nome: "))
nasc = int(input("Ano de nascimento: "))
pessoa["Idade"] = datetime.now().year - nasc
pessoa["CTPS"] = int(input("Carteira de Trabalho: (0 nao tem)"))
if pessoa["CTPS"] != 0:
    pessoa["Contratação"] = int(input("Ano de Contratação: "))
    pessoa["Salário"] = float(input("Salário: R$"))
    pessoa["Aposentadoria"] = pessoa["Idade"] + ((pessoa["Contratação"] + 35) - datetime.now().year)
print("_" * 50)
for x, y in pessoa.items():
    print(f" - {x} tem o valor {y}")