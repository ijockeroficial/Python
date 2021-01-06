casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual seu salário? "))
ano = int(input("Em quantos anos vai pagar? "))
#Calculando quantos meses tem a quantidade de anos informado.
meses = ano * 12
#Calculo da prestação mensal.
prestacao = casa / meses

if prestacao <= salario * 0.3:
    print("A prestação mensal é de: {}".format(prestacao))
else:
    print("Emprestimo negado!")