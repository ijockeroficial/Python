import random

inicio = 0
lista = []
numero = 0
#Primeiro jeito de fazer um gerador de números da MegaSena.
while(inicio <= 5):
    inicio += 1
    numero = random.randrange(1,60)
    if(numero not in lista):
        lista.append(numero)
    else:
        inicio -=1
                       
#Segundo jeito de fazer um gerador de números da MegaSena
def gerar6Numeros(listaPython):
    if(len(listaPython) < 6):
        numero = random.randrange(1,60)
        if(numero not in listaPython):
            listaPython.append(numero)
            gerar6Numeros(listaPython);
        else:
            gerar6Numeros(listaPython);
    else:
        return;


lista2 = []
gerar6Numeros(lista2);


print("#" * 30 + " v1.0 " + "#" * 30) 
print("_" * 65)
print("                 __  __                    ____                   ")
print("                |  \/  | ___  __ _  __ _  / ___|  ___ _ __   __ _ ")
print("                | |\/| |/ _ \/ _` |/ _` | \___ \ / _ \ '_ \ / _` |")
print("                | |  | |  __/ (_| | (_| |  ___) |  __/ | | | (_| |")
print("                |_|  |_|\___|\__, |\__,_| |____/ \___|_| |_|\__,_|")
print("                             |___/  ")
print("_" * 47 +" By iJockerOficial")
print("GitHub: https://github.com/iJockerOficiaL")
print(" " * 65)
print("-" * 10 + ">" + " " * 10 + "{}".format(lista)+" " * 10 + "<" + "-" * 10)
print("-" * 10 + ">" + " " * 10 + "{}".format(lista2)+" " * 10 + "<" + "-" * 10)
print("_" * 66)
print("")
print("#" * 66) 