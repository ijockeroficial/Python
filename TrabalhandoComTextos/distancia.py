distancia = float(input("Qual é a distância da sua viagem? "))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print("O preço da sua passagem é de: {} ".format(preco))