frase = ('curso de análise e desenvolvimento de sistemas')
print (frase [3]) #isso mostra o espaço da memória
print (frase [3:46]) #intervalo de caracteres menos o ultimo
print (frase [3:46:2]) #pula de dois em dois
print (frase [:34]) #pega do inicio até o caracter que vc escolheu
print (frase [34:]) #pega do caracter que vc escolheu até o final
print (frase [3::6]) #pega do caracter que vc escolheu pulando de 3 em 3
print (len(frase))  #esse metodo conta a quantidade de caracteres
print (frase.count('a')) #count procura um caracter especifico na variavel
print (frase.count('t',3,46)) #caracter especifico dentro de um intervalo especifico
print (frase.find('curso')) #o find mostra a partir de qual indice aparece a pesquisa
print (frase.find ('android')) #o resultado -1 indica que não tem essa sequencia na variavel
print ('android'in frase) # o in verifica se aquele conjunto de string esta na variavel
print (frase.replace('curso','t.i')) #troca a palavra
print (frase.upper()) #deixa em maiuscula
print (frase.lower()) #deixa em minusculo
print (frase.capitalize()) #deixa a primeira letra da primeira palavra em maiusculo
print (frase.title()) #deixa todas as letras em maiusculo
print (frase.strip()) #tira o espaço em brando do inicio e do final
print (frase.rstrip()) #tira o espaço do lado direito
print (frase.lstrip()) #tira o espaço do lado esquerdo
print (frase.split()) #transformar o valor da variavel em lista
print ('*'.join(frase)) #une um simbolo em cada parte do split