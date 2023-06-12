def main():
    class Vehiculo():
        def __init__(self, color, ruedas):
            self.color = color
            self.ruedas = ruedas
      
        def __str__(self) -> str:
            return f'Color: {self.color}\nRuedas: {self.ruedas}'
        
    vehiculo = Vehiculo("rojo", 4)
    f = open("vehiculos.txt", "w")
    f.write(vehiculo.__str__())
    f.close()

if __name__ == "__main__":
    main()