#Programa para classificar o IMC d euma pessoa
#Author: Nicole Matos
#Data: 20/05/2026

imc = 0 

peso = float(input('Digite o seu peso:'))
altura = float(input('Digite a sua altura:'))

imc = peso / altura**2

if imc < 16:
    print('Magreza leve')
elif imc <17:
    print('Magreza moderada')
elif imc < 18.5:
    print( 'Magreza leve')
elif imc <25:
    print("Saudável")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print('Obesidade Grau I')
elif imc < 40:
    print('Obesidade Grau II')
else:
    print('Obesidade Grau III')