#Programa para ler a idade em anos, meses e dias e mostrar quantos dias ela viveu
#Author: Nicole Matos
#Data: 20/05/2026

anos = int(input('Quantos anos você já viveu? \n'))
meses = int(input('Quantos meses você tem? \n'))
dias = int(input('Quantos dias você tem? \n'))

dTotal = anos * 365 + meses * 30 + dias

print('Você já viveu {} dias.'.format(dTotal))