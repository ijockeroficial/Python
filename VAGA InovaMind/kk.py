lista = [[1993, 2030], [2000, 2060], [1992, 1997], [1996, 2020]]

def pegar_ano_inicio(elem):
    return elem[0]

def pegar_ano_fim(elem):
    return elem[1]

lista.sort(key=pegar_ano_inicio)
print(lista)
x = map(pegar_ano_fim,lista)
menor_ultimo_ano_trabalhado = min(x)
print("Menor Saida" + str(menor_ultimo_ano_trabalhado))
inicio_periodo_com_mais_pessoas_trabalhando = 0
fim_periodo_com_mais_pessoas_trabalhando = 0

for x in lista:
    
    print(x)
    print(lista.index(x))
    if(lista.index(x) == (len(lista)-1)):
        break

    if int(x[0]) < lista[lista.index(x) +1][0] and x[0] <= menor_ultimo_ano_trabalhado:
        print("entrou")
        inicio_periodo_com_mais_pessoas_trabalhando = x[0]
        fim_periodo_com_mais_pessoas_trabalhando = menor_ultimo_ano_trabalhado


print("Periodo mais trabalhado " + str(inicio_periodo_com_mais_pessoas_trabalhando) + " - " + str(fim_periodo_com_mais_pessoas_trabalhando))

    



#for x in lista:
    #if lista.index(x) < len(lista):
        #proximo_elemento = lista.index(x+1)
    
        #if(proximo_elemento[0]):
    

