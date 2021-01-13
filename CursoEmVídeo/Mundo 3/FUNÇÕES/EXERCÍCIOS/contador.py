from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print("_" * 50)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")

    if inicio < fim:
        for x in range(inicio, fim + 1, passo):
            print(f"{x}", end=" ", flush=True)
            sleep(0.5)
        print("FIM!")
    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont}", end=" ", flush=True)
            sleep(0.5)
            cont -= passo
        print("FIM!")
    

contador(1, 10, 1)
contador(10, 0, 2)
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i, f, p)