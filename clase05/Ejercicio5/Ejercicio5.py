def es_bisiesto(year):
    if year % 4 == 0 and (year % 100 != 0):
        return f'{year} es un año bisiesto'
    else:
        return f'{year} no es un año bisiesto'
    
print(es_bisiesto(2023))