while True:
    num = int(input('digite a sua tabuada'))
    if num < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num * c}')
    print('-' * 30)
print('acabou')
