# Objetos

# clase dinamica
class Dino:
    encendido = False

    def enciende(self):
        self.encendido = True # hace referencia a la variable de la clase
    
d = Dino()
d.enciende()
print(d.encendido)

# clase estatica
class Opciones:
    servidor_seguro = True
    reiniciar = False

if Opciones.servidor_seguro:
    print("Todo bien")

# herencia
class Juguete(Dino):
    quitar_oreja = True

print(Juguete.encendido)

# constructores

class Persona:
    def __init__(self, nombre, edad): # constructor = palabra reservada init
        self.nombre = nombre
        self.edad = edad

# clases abstractas
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def comer(self):
        pass

class Perro(Animal):
    pass

# Relaciones HAS-A
class Motor:
    pass

class Chasis:
    motor: Motor()
    pass

class Ventanas:
    pass

class Auto:
    chasis: Chasis()
    ventanas: Ventanas()
    pass

c = Auto()
print(c.chasis.motor)