dados = []
pessoas = []
valor = True
while valor:
    dados.append(str(input("Nome: "))) #Recebe o nome da pessoa.
    dados.append(float(input("Peso: "))) #Recebe o peso da pessoa.
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:]) #Faz uma cópia da lista "dados" para a lista "pessoas".
    dados.clear() #Limpa os dados da lista "dados".
    continuar = str(input("Quer continuar? S/N ")).strip().upper()
    if continuar == "S":
        valor = True
    else:
        if continuar == "N":
            valor = False
print("_" * 30)
qnt = len(pessoas) #Conta a quantidade de itens dentro da lista.
print(f"{qnt} foram cadastradas!")
print(f"O maior peso foi de {mai}kg", end=" ")
for p in pessoas:
    if p[1] == mai:
        print(f"[{p[0]}]", end=" ")
print(f"O menor peso foi de {men}kg", end=" ")
for p in pessoas:
    if p[1] == men:
        print(f"[{p[0]}]", end=" ")
'''
dados = []
pessoas = []
valor = True
while valor:
    dados.append(str(input("Nome: "))) #Recebe o nome da pessoa.
    dados.append(int(input("Peso: "))) #Recebe o peso da pessoa.
    pessoas.append(dados[:]) #Faz uma cópia da lista "dados" para a lista "pessoas".
    dados.clear() #Limpa os dados da lista "dados".
    continuar = str(input("Quer continuar? S/N ")).strip().upper()
    if continuar == "S":
        valor = True
    else:
        if continuar == "N":
            valor = False
qnt = len(pessoas) #Conta a quantidade de itens dentro da lista.
print(f"{qnt} foram cadastradas!")
pesadas = []
leves = []
for p in pessoas:
    if p[1] > 50:
        pesadas.append(p[0])
    else: 
        leves.append(p[0])
print(f"As pessoas mais pesadas são: {pesadas}")
print(f"As pessoas mais leves são: {leves}")
'''