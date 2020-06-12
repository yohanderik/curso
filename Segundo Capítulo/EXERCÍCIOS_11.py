#1_ (DESAFIO) Este exercício, assim como outros que virão em outros capítulos, é considerado um desafio, porque ele é relativamente mais difícil do que outros do mesmo capítulo. Assim, ele é algo que você deveria tentar fazer; mas não se frustre se não conseguir, porque é mais difícil mesmo. Agora, se você conseguir resolver os desafios, parabéns, você provavelmente tem um belo futuro pela frente no mundo da programação de computadores. Então, lembra-se da equação de Báscara da escola, que se usa para calcular as duas raízes de um polinômio? Escreva um programa que leia os valores de “a”, “b” e “c”, para a equação ax2 + bx + c = 0 e calcule as duas raízes desse polinômio usando a fórmula de Báscara: x = -b ± b2-4ac22a. Lembre-se que são dois valores para “x”, um quando o sinal “±” é interpretado como soma e outro quando “±” é interpretado como subtração.

#R_

import math

print('Esse programa calculara a formula de bascara')

A = int(input('O valor de A e igual a:   '))

B = int(input('O valor de B e igual a:   '))

C = int(input('O valor de C e igual a:   '))

#math.sqrt = raiz quadrada

#X = (-B +- math.sqrt(B ** 2 - 4 * A * C)) / 2 * A

#math.sqrt(4) == 4 ** (1/2)

delta = (B ** 2 - 4 * A * C) ** (1/2)

X1 = (-B + delta) / (2 * A)

X2 = (-B - delta) / (2 * A)

print('A primeira raiz e igual a:', X1)

print('A segunda raiz e igual a:', X2)

print(A * X1 ** 2 + B * X1 + C)

print(A * X2 ** 2 + B * X2 + C)