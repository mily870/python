#valor = int(input("qual o valor para sacar?"))
#cedulas = [100, 50, 5, 2]
#print("cédulas entregues")
#for cedula in cedulas:
    #qtd_cedulas = valor // cedula
    #valor %= cedula
    #print(f"R$ {cedula}: {qtd_cedulas} cédula")
#if valor > 0:
    #print(f"não foi possível sacar R$ {valor} por falta de cédulas menores")

FLAG = 757
contador = 0
multiplicacao = 1
print(f"digite vários números inteiros e para parar digite {FLAG}.")
while True:
    numero = int(input("Digite um número: "))
    contador += 1
    multiplicacao *= numero
    if numero == FLAG:
        break
print("resultado final")
print(f"total de números {contador}")
print(f"a multiplicação é {multiplicacao}")
