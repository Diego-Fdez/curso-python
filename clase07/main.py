import operaciones as o #importación de módulos
from divisor import operador #importación de paquetes

def main():
    sum = o.suma(2,3)
    print(sum)

    res = o.resta(3, 2)
    print(res)

    multiplicador = o.Operador()
    print(multiplicador.multiplicador(2, 3))

    div = operador.division(4, 2)
    print(div)

if __name__ == '__main__':
    main()