aluno = {}
aluno["nome"] = str(input("Nome do Aluno: ")).strip().upper()
aluno["média"] = float(input("Média do Aluno: "))
if aluno["média"] >= 7:
    aluno["situação"] = "Aprovado"
elif 5 <= aluno["média"] < 7:
    aluno["situação"] = "Recuperação"
else:
    aluno["situação"] = "Reprovado"
print("_" * 50)
for k, v in aluno.items():
    print(f" - {k} é igual a {v}")