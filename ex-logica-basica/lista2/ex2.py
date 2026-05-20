#Programa para simular o funcionamneto de uma calculadora
#Author:Nicole Matos
#Data: 20/05/2026

#inicialização
result = 0

#entrada do user
opera = str(input('Escolha a operação que você deseja efetuar no seguinte formato: (A-adição/ S-subtração/ M-multiplicação/ D-divisão)\n\n'))
num1 = int(input('Digite o 1° número da operação:\n'))
num2 = int(input('Digite o 2°número da operação:\n '))

#processamento + saída
if opera == 'A':
    result = num1 + num2
    print('O resultado da operação é: {}'.format(result))
elif opera == 'S':
    result = num1 - num2
    print('O resultado da operação é: {}'.format(result))
elif opera == 'M':
    result = num1 * num2
    print('O resultado da operação é: {}'.format(result))
elif opera == 'D':
    result = num1 / num2
    print('O resultado da operação é: {}'.format(result))
else:
    print('Selecione uma operação válida!!')