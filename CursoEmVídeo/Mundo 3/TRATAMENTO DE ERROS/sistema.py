from modulos.arquivo import *
from modulos.interface import menu, linha, cabecalho, leiaInt
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver Pessoas", "Cadastrar Pessoas", "Sair do Sistema"])
    if resposta == 1:
        #Opçao de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabecalho("Saindo...")
        break
    else:
        print("\033[0;31mERRO! Digite uma opção válida!\033[m")
        sleep(2)