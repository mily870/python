#valor = int(input("qual o valor para sacar?"))
#cedulas = [100, 50, 5, 2]
#print("cédulas entregues")
#for cedula in cedulas:
    #qtd_cedulas = valor // cedula
    #valor %= cedula
    #print(f"R$ {cedula}: {qtd_cedulas} cédula")
#if valor > 0:
    #print(f"não foi possível sacar R$ {valor} por falta de cédulas menores")

#FLAG = 757
#contador = 0
#multiplicacao = 1
#print(f"digite vários números inteiros e para parar digite {FLAG}.")
#while True:
    #numero = int(input("Digite um número: "))
    #contador += 1
    #multiplicacao *= numero
    #if numero == FLAG:
        #break
#print("resultado final")
#print(f"total de números {contador}")
#print(f"a multiplicação é {multiplicacao}")


#frase = input("digite uma frase").strip().upper()
#quantidade = frase.count("E")
#ultima_posicao = frase.rfind("E") + 1
#print(f"a letra 'E' aparece {quantidade} vezes na frase")
#if quantidade > 0:
    #print(f"a letra 'E' aparece pela última vez na posição {ultima_posicao}")
#else:
    #print("a letra 'E' não aparece na frase")

import random
numero_computador = random.randint(0, 9)
tentativa = int(input("digite um numero entre 0 a 9"))
if tentativa == numero_computador:
    print(f"acertou, o número era {numero_computador}.")
    print("computador perdeu")
else:
    print(f"errou, eu tinha pensado no número {numero_computador}.")
    print("computador ganhou")