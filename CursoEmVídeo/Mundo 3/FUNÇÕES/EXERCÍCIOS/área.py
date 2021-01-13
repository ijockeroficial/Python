def área(largura, comprimento):
    área = largura * comprimento
    print(f"A área de um terreno {largura}x{comprimento} é {área}m²")


a = float(input("Informe o valor da largura do terreno: "))
b = float(input("Informe o valor do comprimento do terreno: "))
área(a, b)
