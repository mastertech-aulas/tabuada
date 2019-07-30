
opicao = int(input('Digite:\n1 - para tabuada completa\n2 - Para tabuada específico\n:'))

if opicao == 1:
    for x in range(1, 11):
        for y in range(1, 11):
            resultado = x*y
            print(x, 'X', y, '=', resultado)
elif opicao == 2:
    numero = int(input('Digite um numero\n:'))

    for x in range(1, 11):
        resultado = numero*x
        print(numero, 'X', x, '=', resultado)