nome=input ('qual é o seu nome?')
print ('prazer em conhece-lo {:20}!'.format (nome)) 
print ('prazer em conhece-lo {:>20}!'.format (nome)) #espaçamento para a direita
print ('prazer em conhece-lo {:<20}!'.format (nome)) #espaçamento para a esquerda
print ('prazer em conhece-lo {:^20}!'.format (nome)) #alinhamento centro

num1=int (input('digite um valor'))
num2=int (input('digite outro valor'))
soma = (num1+num2) #criar a variável quando utilizar em outra parte do código
print ('a soma é {}'.format(soma))
