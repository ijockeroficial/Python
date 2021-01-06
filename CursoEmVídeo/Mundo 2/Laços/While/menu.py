num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
print("Escolha uma das opções abaixo:")
print('''
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair
''')
opcao = int(input("Digite o número da opção escolhida: "))
while opcao != 5:
    if opcao == 1:
        print("O resultado da soma é: {}".format(num1+num2))
        break
    elif opcao == 2:
        print("O resultado da multiplicação é: {}".format(num1*num2))
        break
    elif opcao == 3:
        if num1 > num2:
            print("O primeiro numero ({}) é maior que o segundo número ({})".format(num1,num2))
            break
        elif num1 == num2:
            print("Os números são iguais")
            break
        else: 
            print("O segundo número ({}) é maior que o primeiro número ({})".format(num2,num1))
            break
    elif opcao == 4: 
        num1 = int(input("Digite o primeiro número inteiro: "))
        num2 = int(input("Digite o segundo número inteiro: "))
        opcao = int(input("Digite o número da opção escolhida: "))
    else: 
        print("Opção inválida") 
        break
