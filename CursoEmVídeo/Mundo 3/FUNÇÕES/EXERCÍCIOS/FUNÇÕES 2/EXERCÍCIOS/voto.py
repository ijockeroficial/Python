from datetime import datetime
def voto(ano):
    idade = datetime.now().year - ano
    if idade > 60 or 16 <= idade < 18:
        return print("VOTO OPICIONAL!")
    else:
        if idade < 18:
            return print("VOTO NEGADO!")
        if idade >= 18:
            return print("VOTO OBRIGATÓRIO!")
    

nasc = int(input("Ano de nascimento: "))
voto(nasc)