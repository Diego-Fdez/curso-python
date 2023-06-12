def miFuncion():
    print('Diego')

def suma(a, b):
    print(a + b)

suma(1, 2)

temperatura = 29.0

def weather():
    global temperatura
    temperatura = 30.5
    print(temperatura)

weather()

print(temperatura)

# named parameters
def nombre(**kwargs):
    if kwargs['name'] == 'Diego':
        print('Hola Diego')

nombre(name='Diego')

# funcion anonima
anonima = lambda x: x * 2

print(anonima(5))

anonima2 = lambda nombre: print(f'Hola {nombre}')

anonima2('Diego')