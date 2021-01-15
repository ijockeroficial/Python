def teste(b):
    global a #Utiliza a variavel "A" global
    a = 8 #O "A" no global passou a ser 8 e na função também
    print(f"O valor de B: {b}") #msm depois de A valer 8 pro B ainda é 5
    #O B recebeu o valor de A que é 5
    b += 4 #.Ai soma +4 e da 9
    c = 2
    print(f"Os valores de B: {b}, C: {c}")


a = 5
print(f"VALO DE A: {a}")
teste(a) #Dps de chamar a funçao o A passa a valer 8
print(f"O A vale: {a}") #Na função o A passou a ser 8