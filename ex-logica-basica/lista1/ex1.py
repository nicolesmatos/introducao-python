# Programa para converter a temperatura lida em C para F
#Author: Nicole Matos
#Data: 20/05/2026

# inicializando as variáveis
tempC = 0
tempF = 0

tempC = float(input('Digite a temperatura em °C que será convertida:\n'))
tempF = tempC * 1.8 + 32

print('{}°C equivale a {}°Fahrenheit'.format(tempC, tempF))



