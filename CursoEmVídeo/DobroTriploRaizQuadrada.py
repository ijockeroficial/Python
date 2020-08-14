#importação a biblioteca math
import math

n = float(input("Digite um número: "))
print("O número é: {}".format(n))
print("O seu dobro é: {}".format(n*2))
print("O seu triplo é: {}".format(n*3))
print("A sua raiz quadrada é: {}".format(n ** 0.5)) 
print("A sua raiz quadrada usando o método POW é: {}".format(pow(n,0.5))) 
print("A sua raiz quadrada é: {}".format(math.sqrt(n)))

#Utilizamos dois métodos o POW e o Math.SQRT