#Tem como fazer assim também:
lista = [["Joao", 20], ["Maria", 15], ["Lucas", 23], ["Benício", 24]]
for x in lista: #O x percorre toda a lista assumindo os valores.
    #Aqui mostra o nome e a idade na posição escolhida em x
    print(f"{x[0]} tem {x[1]} anos")
print("_" * 50)
dado = list()
galera = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:]) #Faz uma cópia da lista.
    dado.clear() #Limpa os dados da lista "dado".
    
for p in galera: #Percorre a lista galera e armazena em P.
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
        totmai += 1 #Serve para contar quantos maiores de idade tem.
    else:
        print(f"{p[0]} é menor de idade.")
        totmen += 1 #Serve para contar quantos menores de idade tem.
print(f"Temos {totmai} maiores e {totmen} menores")