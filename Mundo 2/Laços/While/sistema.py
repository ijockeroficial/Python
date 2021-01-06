produto_nome = str(input("Informe o nome do produto: "))
preço_produto = float(input("Informe o preço do produto: "))
total = maior_que_mil = mais_barato = contagem = 0
continuar = "S"
barato = " "
while continuar != "N":
    total += preço_produto
    if preço_produto >= 1000:
        maior_que_mil += 1
    if contagem == 1 or preço_produto < mais_barato:
        mais_barato = preço_produto
        barato = produto_nome
    continuar = str(input("Quer continuar? S/N ")).strip().upper()[0]
    if continuar == "N":
        break
    elif continuar == "S": 
        produto_nome = str(input("Informe o nome do produto: "))
        preço_produto = float(input("Informe o preço do produto: "))
        contagem +=1
    else: 
        continuar == "S"
        print("Você informou uma resposta inválida! Vamos continuar...")
print("O total gasto nas compras foi de: R${}".format(total))
print("{} produtos custam mais de R$1000,00".format(maior_que_mil))
print("O nome do produto mais barato é: {} ".format(barato))