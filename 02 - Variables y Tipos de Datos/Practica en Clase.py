print('Hola Mundo!!!!!!!!!')
#1.- Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
variable_entera = 1234
print(variable_entera)
#2-.Imprimir el tipo de dato de la constante 8.5
print(type(8.5))
#3.-Imprimir el tipo de dato de la variable creada en el punto 1
print(type(variable_entera))
#4.- Crear una variable que contenga tu nombre
mi_variable = 'Ofelia'
#5.- Crear una variable que contenga un número complejo
numero_complejo = 30.5j
#6.- Mostrar el tipo de dato de la variable crada en el punto 5
print(type(numero_complejo))
#7.- Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
pi = 3.14161819
pi_redondeado = round(pi,4)
print(pi_redondeado)
#8.- Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
#son diferentes ya que variable 1 es un tipo boleano y variable 2 es una cadena de caracteres
variable1 = True
variable2 = 'True'
#9.- Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print(type(variable1))
print(type(variable2))
#10.- Asignar a una variable, la suma de un número entero y otro decimal
variable = 5 + 6.8
#11.- Realizar una operación de suma de números complejos
suma_compleja = 5j + 6j
#12.- Realizar una operación de suma de un número real y otro complejo
suma = 67 + 6j
#13.- Realizar una operación de multiplicación
multiplicacion = 6 * 8
#14.- Mostrar el resultado de elevar 2 a la octava potencia
potenciacion = 2**8
print(potenciacion)
#15.- Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
variable_cociente = 27/4
print(variable_cociente)
#16.- De la división anterior solamente mostrar la parte entera
variable_division_entera = 27//4
print(variable_division_entera)
#17.- De la división de 27 entre 4 mostrar solamente el resto
variable_division_resto = 27%4
print(variable_division_resto)
#18.- Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
variable_division = (variable_division_entera*4)+variable_division_resto
print(variable_division)
#19.- Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
variable_a = 'hola'
variable_b = 'mundo!!!!'
print(variable_a + variable_b)
#20.- Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?, son diferentes tipos de datos, cadena y entero
variable_c='2'
variable_d=2
type(variable_c)
type(variable_d)
#21.- Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
variable_c = int(variable_c)
print(variable_c==variable_d)
#22.- ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
#muestra error porque no puede convertir el tipo de dato cadena a tipo de dato flotante
a=float('3,8')
#23.- Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
x = 3
x-=1
print( x)
#24.- Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print(2<<3)
#25.- Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
#No se permite la operacion porque son de diferente tipo
print (2 + '2')
#26.- variable_f = 2
variable_f = 2
variable_g = '2'
variable_g=int(variable_g)
print(variable_f+variable_g)
