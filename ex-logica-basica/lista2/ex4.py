#Programa para ler os 3 lados de um triângulo e classificá-lo em equilátero, isóscele e escaleno
#Author: Nicole Matos
#Data: 20/05/2026


l1 = int(input('Digite o lado 1 do triângulo:\n'))
l2 = int(input('Digite o lado 2 do triângulo: \n'))
l3 = int(input('Digite o lado 3 do triângulo: \n'))

if l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1:
    print('Não forma um triângulo')
else:
    if l1 == l2 and l2 == l3:
        print('O triângulo é equilátero')
    elif l1 != l2 and l1 != l3  and l2 != l3:
        print('O triângulo é escaleno')
    else:
        print('O triângulo é isósceles')

