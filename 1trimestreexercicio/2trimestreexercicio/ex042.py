nota1 = float(input("digite a primeira nota"))
nota2 = float(input("digite a segunda nota"))
media = (nota1 + nota2) / 2
if media < 5:
    print("Resultado: reprovado")
elif media >= 5 <= 6.9:
    print("resultado: recuperação")
else:
    print("resultado: aprovado")