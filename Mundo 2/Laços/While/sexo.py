''' sexo = "M"
while sexo == "M":
    sexo = str(input("Informe seu sexo M ou F: ")).upper().strip()
    if sexo == "M":
        print("Você é Homem")
        break
    elif sexo == "F":
        print("Você é mulher")
        break
    else: 
        sexo = "M"
'''
#Correção.
sexo = str(input("Informe seu sexo: [M/F] ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ")).strip().upper()[0]
print("Sexo {} registrado com sucesso!".format(sexo))