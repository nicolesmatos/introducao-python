#Programa para converter o Real para o Dólar, Euro ou Iene a partir da escolha do usuário
#Author: Nicole Matos
#Data: 20/05/2026

#declaração das constantes
dolar = 0.2
euro = 0.17
iene = 31.66
conversao = 0

#entrada do usuário
escolha = str(input('Escolha a moeda de conversão (D-dólar/ E-euro/ I-iene)'))
real = float(input('Digite o valor em Real que será convertido: \n'))

if escolha == 'D':
    conversao = real * dolar
    print("{} reais valem {:.2f} dólares".format(real,conversao))
elif escolha == 'E':
    conversao = real * euro
    print("{} reais valem {:.2f} euros".format(real,conversao))
elif escolha == 'I':
    conversao = real * iene
    print("{} reais valem {:.2f} ienes".format(real,conversao))
else :
    print('Digite um valor válido de entrada')



