times = ("Cruzeiro", "Atletico-MG", "São Paulo", "Corinthians", "Chapecoense", "Flamengo", "América-MG", "Botafogo", "Santos", "Fluminense")
x = 1
print("Os cinco primeiros times são: ")
while x <= 5:
    print("{}".format(times[x]))
    x+=1
print("Os 4 últimos colocados são: ")
x = 6
while x > 5:
    if x < 10:
        print("{}".format(times[x]))
    else: break
    x+=1
print("A {}".format(times[4]), "ta na posição: 4")

#Correção:
'''
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)

print(f'Os 5 primeiros times são {times[0:5]}')
print(f'Os 4 últimos times são {times[-4:]}')
print(f'Os times em ordem alfabetica são {sorted(times)}')
print(f'Posição da Chapecoense: '.format(times.index("Chapecoense")+1))
'''