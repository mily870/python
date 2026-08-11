numero = ('zero' , 'um' , 'dois' , 'tres' , 'quatro' , 'cinco' , 'seis' , 'sete' , 'oito' , 'nove' , 'dez' , 'onze' , 'doze' , 'treze' , 'quatorze' , 'quinze' , 'dezesseiss' , 'dezessete' , 'dezoito' , 'dezenove' , 'vinte')

digitado = int (input('digite um numero entre 0 e 20'))

while True:
    if digitado < 0 or digitado > 20:
        digitado = int (input('tente novamente'))
    else:
        break

print(f'vc digitou o numero {numero[digitado]}')
