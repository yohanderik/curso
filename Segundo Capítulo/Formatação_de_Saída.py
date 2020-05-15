x = 31827
y = 87

print(x, '//', y, '=', x // y)
print(x, '%', y, '=', x % y)                              #Estilo menos recomentadovel

print('{0} // {1} = {2}' .format(x, y, x // y))           
print('{0} % {1} = {2}' .format(x, y, x % y))             #Estilo mais recomentavel

#x.mensagem(y)                Errado
#mensagem(x,y)                Certo