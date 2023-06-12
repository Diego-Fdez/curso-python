class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    
    def __str__(self):
        return f"Color: {self.color} Ruedas: {self.ruedas} Puertas: {self.puertas}"

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Color: {self.color} Ruedas: {self.ruedas} Puertas: {self.puertas} Velocidad: {self.velocidad} Cilindrada: {self.cilindrada}"
    
auto = Coche('verde', 4, 4, 145, 1800)

print(auto)

