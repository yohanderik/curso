#1_ Você gostaria de saber quantos segundos se passaram desde a meia-noite? Escreva um programa que leia valores inteiros para hora, minuto e segundo. Em seguida, o programa deve calcular e imprimir quantos segundos se passaram no total desde a última meia-noite até a hora lida. Deixamos a fórmula por sua conta

#R_

print('Este programa lhe darar quanto tempo se passou deste a meia-noite em segundos.')

HORAS = int(input('Define as HORAS:   '))

MINUTOS = int(input('Define os MINUTOS:   '))

SEGUNDOS = int(input('Define os SEGUNDOS:   '))

print('Ja se passaram', SEGUNDOS + MINUTOS * 60 + HORAS * 60 ** 2, 'segundos deste a meia-noite')