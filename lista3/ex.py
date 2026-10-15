/#

Author: Nicole Matos
Date: 14/10/2026
Descripton: Programa para bilheteria inteligente

Entrada Proibida: Se o visitante tiver altura menor que 1.20m ou idade menor que 6 anos, ele não pode entrar em nenhum brinquedo radical (exiba uma mensagem customizada informando o motivo).

Gratuidade: Têm entrada gratuita:

Crianças menores de 10 anos (desde que tenham altura para entrar).

Idosos com 60 anos ou mais.

Regra VIP / Desconto: Quem não for morador da cidade sede (!=) paga a taxa inteira de R$ 50,00. Moradores pagam meia (R$ 25,00), a menos que tenham um cupom de sócio (True ou False), caso em que a entrada é gratuita mesmo sendo morador.

#/

#entrada dos dados

altura = float(input('Digite sua altura em M: '))
idade = int(input('Digite sua idade'))
morador = str(input('Digite a cidade em que você reside'))
cupom = int(input('Digite 1 se tiver um cupom de sócio e 0 se não tiver cupom'))
cidade_sede = 'Barueri'

if altura  < 1.2 or idade < 6:
    print('Você não pode entrar porque não possui a altura ou a idade mínima permitida')
elif idade < 10 or idade > 60:
    printf('A sua entrada é gratuita!\n Aproveite o parque!')
elif morador == cidade_sede and cupom == 1:
    printf('A sua entrada é gratuita!\n Aproveite o parque!')
elif morador == cidade_sede:
    print('Sua entrada é meia custa R$25,00')
else print('Sua entrada é inteira  ecusta R$50,00')
