#Exercício de fixação.
nome = str(input("Digite seu nome completo: "))
#Nome com todas as letras maiúsculas.
print(nome.upper())
#Nome com todas as letras minúsculas.
print(nome.lower())
#Quantas letras ao todo sem contar espaços.
nome2 = nome.split()
cont1 = len(nome2[0])
cont2 = len(nome2[1])
cont3 = len(nome2[2])
soma = cont1+cont2+cont3
print(soma)
#Quantas letras tem o primeiro nome?
print("O primeiro nome tem: {} letras".format(len(nome2[0])))