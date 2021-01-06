#Correção:
produtos = ["Livro", 12.00, "Caneta", 2.00, "Carne", 22.00, "Suco", 2.00, "Macarrao", 6.00, "Ferro", 40.00]

print('-' * 40)
print(f'{"PRODUTOS":^40}')
print('-' * 40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end=' ')
    else: print(f'R${produtos[pos]:>5}')

'''
tabela = []
for x in range(0, 4):
    produto = str(input("Informe um produto: "))
    preço = str(input("Informe o preço: "))
    tabela += [produto, preço]
print("{}.....................R$ {}".format(tabela[0], tabela[1]))
print("{}.....................R$ {}".format(tabela[2], tabela[3]))
'''