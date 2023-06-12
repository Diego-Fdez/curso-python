class Alumno:
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota)

    def resultado(self):
        if self.nota < 65:
            print("El alumno ha suspendido")
        else:
            print("El alumno ha aprobado")

alumno = Alumno()

alumno.inicializar("Diego",90)
alumno.imprimir()
alumno.resultado()