from operator import itemgetter
def notasAluno(nota):
    maior = max(nota)
    menor = min(nota)
    cont = len(nota)
    media = sum(nota) / cont
    notas2 = {"Maior Nota":maior, "Menor Nota":menor, "Quantidade de Notas":cont,"Média das Notas":media}
    if media > 7:
        notas2["Situação"] = "APROVADO"
    else:
        if media < 7:
            notas2["Situação"] = "REPROVADO"
    print(notas2)
            

 


notas = []
while True:
    notas.append(float(input("Nota: ")))
    parar = str(input("Deseja parar? S/N ")).strip().upper()[0]
    if parar == "S":
        break
notasAluno(notas)
