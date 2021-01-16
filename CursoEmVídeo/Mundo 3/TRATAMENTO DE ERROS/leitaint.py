def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mERRRO! Digite um número inteiro válido. \033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[0;31mUsuário preferiu não digitar esse número. \033[m")
            return 0
        else:
            return n



n = leiaInt("Digite um número: ")
print(f"Você digitou o número {n}")