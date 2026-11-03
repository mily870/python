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

# import random
# numero_computador = random.randint(0, 9)
# tentativa = int(input("digite um numero entre 0 a 9"))
# if tentativa == numero_computador:
#     print(f"acertou, o número era {numero_computador}.")
#     print("computador perdeu")
# else:
#     print(f"errou, eu tinha pensado no número {numero_computador}.")
#     print("computador ganhou")

# Inicializa a lista vazia para guardar os dados das pessoas
 

# dados = []
# for i in range(1, 5): 
#     print(f"Dados da Pessoa {i}") 
#     altura = float(input("digite a altura: ")) 
#     idade = int(input("digite a idade: ")) 
#     pessoa = { 
#         "altura": altura, 
#         "idade": idade 
#     } 
#     dados.append(pessoa) 
# print() 
# print("Lista de pessoas armazenadas:") 
# print(dados)

# lista = []
# lista.append("arroz")
# lista.append("feijão")
# lista.append("leite")
# lista.append("pão")
# lista.append("café")
# print(lista)


# texto = "[[prog]ram]a"
# pontos = 0
# erro = 'false'
# for letra in texto:
#     if letra == '[':
#         pontos = pontos + 1
#     elif letra == ']':
#         pontos = pontos - 1
#     if pontos < 0:
#         deu_erro = True
#         break
#     if pontos == 0 and erro == 'false':
#        print("true")  
# else:
#        print("false")


clube = {}
clube['nome'] = input("Digite o nome do clube: ")
clube['ano_fundacao'] = int(input("Digite o ano de fundação: "))
clube['titulos'] = int(input("Digite a quantidade de títulos ganhos: "))
ano_centenario = clube['ano_fundacao'] + 100
print("informações do clube")
print(f"Nome: {clube['nome']}")
print(f"ano de fundação: {clube['ano_fundacao']}")
print(f"quantidade de títulos: {clube['titulos']}")
print(f"o {clube['nome']} completará 100 anos em: {ano_centenario}")


jogadores = {}
for i in range(1, 7):
    nome = input(f"digite o nome do jogador {i}: ")
    resultado = float(input(f"digite o resultado do jogador {i}: "))
    jogadores[nome] = resultado
print("resultado armazenados")
print(jogadores)
ranking_decrescente = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)
print("ordem decrescente (maior para o menor)")
for jogador, resultado in ranking_decrescente:
    print(f"{jogador}: {resultado}")
ranking_crescente = sorted(jogadores.items(), key=lambda item: item[1])
print("ordem crescente (menor para o maior)")
for jogador, resultado in ranking_crescente:
    print(f"{jogador}: {resultado}")


numero = input("digite um número inteiro")
for caractere in numero:
    if caractere.isdigit():
        algarismo = int(caractere)
        if algarismo % 2 == 0:
            print(f"o algarismo {algarismo} é par")
        else:
            print(f"o algarismo {algarismo} é impar")
