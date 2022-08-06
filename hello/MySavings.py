#Tiene que recibir el pago quincenal y luego devolver el el porcentaje
#segun el rebajo que se le tenga que hacer, 
#Rebajo #1 40% Pagos fijos
#Rebajo #2 30% transporte
#Rebajo #3 20% Comida
#Rebajo #4 10% Para lo que sea
# Lo que sobre cada mes se debe guardar en una variable con la cantidad de ahorro del mes pasado, ahorro total y mes y anio
#moneda es en dolares
quincena = 0
ahorroUno = 0
ahorroDos = 0
ahorroTres = 0
ahorroCuatro = 0

ahorroTotal = 0
ahorroMensual = 0

salario = 890

ahorroUno = salario * 40 / 100
ahorroDos = salario * 30 / 100
ahorroTres = salario * 20 / 100
ahorroCuatro = salario * 10 / 100

print('Ahorro 40% Pagos fijos')
print(ahorroUno)

print('Ahorro 30% transporte')
print(ahorroDos)

print('Ahorro 20% Comida')
print(ahorroTres)

print('Ahorro 10% Para lo que sea')
print(ahorroCuatro)

