# if statement
if(5 > 5):
    print("5 is greater than 4")
elif 5 == 4:
    print("5 is equal to 4")
else:
    print("5 is not greater than 4")

# while loop
i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# for loop
lista = [1, 2, 3, 4, 5]

for i in lista:
    print(i)

for i in range(5, 11):
    print(i)

for i in range(len(lista)):
    print(lista[i])

new_list = ['hola', 'mundo', 'python']

for i in new_list:
    if i == 'mundo':
        print(i)
        break

if 'mensaje' not in new_list:
    print("mensaje no esta en la lista")