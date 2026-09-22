matriz = [[0,0,0], [0,0,0], [0,0,0]]
total3 = maior = somapar = 0
for l in range(0, 3): 
    for c in range(0, 3): 
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ')) 
        if matriz [l] [c] %2 == 0:
            somapar += matriz [l] [c]
        if c ==2:
            total3 +=matriz [l] [c]
        if l == 1 and c == 0:
            maior = matriz [l] [c]
        elif l ==1 and c != 0 and matriz [l] [c] > maior:
            maior = matriz [l] [c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()
print (f'a soma dos valores pares é {somapar}')
print (f'a soma dos numeros da terceira coluna é {total3}')
print (f'o maior valor da segunda linha é {maior}')