input = input('Cual es tu peso en kg y tu altura en cm?')
print(input)

input_list = input.split()
peso = float(input_list[0])
altura = float(input_list[1]) / 100
imc = peso / altura ** 2
print('Tu índice de masa corporal es: ' + str(round(imc, 2)))