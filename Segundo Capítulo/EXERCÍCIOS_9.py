#1_ Você está envolvido em um projeto de engenharia e precisa calcular a quantidade de piso para uma sala a ser construída, bem como a quantidade de tinta a ser usada nas paredes. Precisa também saber qual o volume da sala em metros quadrados para estimar a potência necessária para o ar condicionado. Para tanto, escreva um programa que leia 3 números correspondendo ao valor da altura, comprimento e largura da sala em metros e em seguida imprima as seguintes informações:

   #• A área do piso da sala:

      #largura* comprimento

   #• O volume da sala:

      #altura* comprimento* largura

   #• A área das paredes da sala:

      #2* altura* largura + 2* altura* comprimento

#R_

print('Calcularei a area e o volume de seu terreno')

ALTURA = int(input('Qual o valor da ALTURA?   '))

LARGURA = int(input('Qual o valor da LARGURA?   '))

PROFUNDIDADE = int(input('Qual o valor da PROFUNDIDADE?   '))

print('A area do piso do seu terreno e igual a:', PROFUNDIDADE * LARGURA)

print('O volume do seu terreno e igual a:', ALTURA * LARGURA * PROFUNDIDADE)

print('A area das paretes do seu terreno e igual a:', 2 * PROFUNDIDADE * ALTURA + 2 * LARGURA * ALTURA)