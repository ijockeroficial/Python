lanche = ["Hambúguer", "Pizza", "Sorvete", "Salgado", "Leite"]
#Mostra quantos itens tem dentro do Array.
print(len(lanche))
#O "X" vai de 0 a a quantidade de itens q tem dentro do Array.
'''
for x in range(0, len(lanche)):
    print("Eu vou comer: {}".format(lanche[x]))
'''
for comida in lanche:
    print(f"Vou comer: {comida}")