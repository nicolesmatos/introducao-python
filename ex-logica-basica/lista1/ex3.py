#Programa para ler a idade e classificar em:
#0-12 criança/ 13-19 adolescente/ 20-60 adulto/ acia 60 idoso
#Author: Nicole Matos 
#Data: 20/05/2026

idade = int(input('Digite  asua idade: \n'))

if idade <=12:
    print('Você é uma criança')
elif idade <=19:
    print('Voc~e é um adolescente')
elif idade <= 60:
    print('Você é um adulto')
else:
    print("Você é um idoso")