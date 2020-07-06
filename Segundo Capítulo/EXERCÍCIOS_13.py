#1_ De forma muito simplificada podemos dizer que um objeto lançado de uma altura “h” próximo ao nível do mar em nosso planeta, desconsiderando o atrito do ar, cairá com uma aceleração constante que é dada por G = 9.80665 m/ s2. Assim, o tempo de queda de um objeto de uma altura “h” pode ser calculado como 2hG2. Considerando que a altura da Torre de Pisa é de aproximadamente 56 metros e a altura da torre de Tóquio é de 333 metros, escreva um programa que calcule o tempo de queda de um objeto do topo até o chão para cada uma dessas duas torres. Defina “G” como uma constante no seu programa. Os resultados estão na resposta online do exercício.

#R_

G = 9.80665

H = 56
T = (2 * H / G) * (1 / 2)

print('O tempo de queda da Torre de Pisa e igual a:', T)

H = 333
T = (2 * H / G) * (1 / 2)

print('O tempo de queda da Torre de Toquio e igual a:', T)