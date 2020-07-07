#1 Você é dono de uma loja que vende produtos. Sua política é de dar desconto para quem compra à vista, vender pelo preço de etiqueta para quem paga em 5 vezes e cobrar juros de quem compra em 10 vezes. Escreva um programa que leia o valor de uma compra e imprima três valores, todos com até duas casas decimais:

#R_

P = float(input('O preço da compra:   '))

print('O valor a vista e de:', round(P * 0.91, 2))
print('O valor da prestação em 5x e de:', round(P / 5, 2))
print('O valor da prestação em 10x e de:', round(P * 1.17 / 10, 2))