from functools import reduce
from getpass import getpass

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def mi_funcion(x):
    if x % 2 == 0:
        return True
    else:
        return False

res = filter(mi_funcion, numeros)
print(list(res))

# con función anónima
result = filter(lambda x: x % 2, numeros)
print(list(result))

# map
def cuadrado(x):
    return x * x

result = map(cuadrado, numeros)
print(list(result))


# con función anónima

resultado = map(lambda x: x * x, numeros)
print(list(resultado))

# reduce
def suma(a, b):
    return a + b

new_result = reduce(suma, numeros)
print(new_result)

# con función anónima
new_resultado = reduce(lambda a, b: a + b, numeros)
print(new_resultado)

#zip
cursos = ['Java', 'Python', 'JavaScript']
asistentes = [100, 200, 300]
demo = zip(cursos, asistentes)
print(list(demo))

#any == some
list_a = [1 == 1, 2 == 2, 3 == 4]
res_any = any(list_a)
print(res_any)

#all == every
list_b = [1 == 1, 2 == 2, 3 == 3]
res_all = all(list_b)
print(res_all)

#round
a = 2.5 # redondea al entero más cercano
print(round(a))

lista = [1, 2, 3, 4, 5, 6, 10, 7, 9 , 8]

# sorted
ordenada = sorted(lista)
print(ordenada)

# reverse
lista_reverse = sorted(lista, reverse=True)
print(lista_reverse)

# función input
a = input('Ingresa tu nombre: ')
print(f'Hola {a}!')

b = input('Ingresa tu password: ')
print(b)