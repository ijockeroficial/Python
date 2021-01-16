def ficha(nome="<desconhecido>", gols=0):
    print("_" * 50)
    print("         FICHA JOGADOR       ")
    return print(f"Nome: {nome}, Gols: {gols}")


nome = str(input("Nome: "))
gols = str(input("Gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)