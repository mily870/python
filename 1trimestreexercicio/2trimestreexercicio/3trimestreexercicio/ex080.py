valores = []
for c in range (0,5):
    valores.append(int(input(f'digite um valor na posição {c} '))) 
print(f'vc digitou os valores {valores}')
print(f'o maior valor digitado foi {max[valores]} na posição {valores.index(max(valores))+1}')
print(f'o menor valor digitado foi {min[valores]} na posição {valores.index(min(valores))+1}')