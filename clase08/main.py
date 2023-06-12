numero = 5
texto = 'Quijote'

# forma antigua de imprimir
print('El número es %d y el texto es %s' % (numero, texto))

# forma normal de imprimir
print('El número es {} y el texto es {}'.format(numero, texto))

# forma nueva de imprimir
print(f'El nÃ®mero es {numero} y el texto es {texto}')

#ficheros
f = open('prueba.txt', 'w')

# r: lectura
# a: append
# w: escritura
# x: crear archivo

datos = f.read()
f.close()