#1_ (DESAFIO) Escreva um programa em que dados “x” segundos fornecidos pelo usuário, sejam fornecidas as quantidades de horas, minutos e segundos.

#R_

import math

print('Esse programa transforma o valor X que sera o valor de segundos e dividira o valor entre horas, minutos e segundos.')

X = int(input('O valor de X em segundos e igual a:   '))

HORAS = math.floor(X / 60 ** 2) 

RESTO_DAS_HORAS = X % 60 ** 2

MINUTOS = math.floor(RESTO_DAS_HORAS / 60)

SEGUNDOS = RESTO_DAS_HORAS % 60

print('São', HORAS, 'horas,', MINUTOS, 'minutos e', SEGUNDOS, 'segundos.')