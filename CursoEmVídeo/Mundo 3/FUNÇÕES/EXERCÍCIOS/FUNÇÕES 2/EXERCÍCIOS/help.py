def ajuda(entrada):
    help(entrada)


comando = ""
while True:
    comando = str(input("Digite >>: "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)