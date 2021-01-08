#A cidade começa com SANTO ou não?
cidade = str(input("Digite um nome de uma cidade: ")).strip()
#Correção:
print(cidade[:5].upper() == "SANTO")
'''
#Fiz assim:
cidade2 = cidade.split()
if cidade2[0] == "SANTO":
    print("Essa cidade inicia com SANTO")
else: 
    print("Essa cidade não inicia com SANTO")

'''