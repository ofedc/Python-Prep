#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
MivariableEntera = 10
print(MivariableEntera)
#2) Imprimir el tipo de dato de la constante 8.5
y=8.5
type(y)
#3) Imprimir el tipo de dato de la variable creada en el punto 1
type(MivariableEntera)
#4) Crear una variable que contenga tu nombre
Minombre="Ofelia"
#5) Crear una variable que contenga un número complejo
a = 5 + 5j
print(a)
#6) Mostrar el tipo de dato de la variable crada en el punto 5
print('La variable a creada en el punto 5 es del tipo: ',type(a))
#7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
pi=3.14165124
piredondeado=round(pi,4)
print(piredondeado)
#8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. 
# ¿Se trata de lo mismo?, son diferentes porque una variable es de tipo cadena y la otra de tipo boleano
v1 = 'True'
v2 = True
#9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print('La variable 1 es de tipo:',type(v1),'y la variable 2 es de tipo:',type(v2))
#10) Asignar a una variable, la suma de un número entero y otro decimal
a=12+12.5
print(a)
#11) Realizar una operación de suma de números complejos
bc=8+2j 
cc=5+ 3j
print(bc+cc)
#12) Realizar una operación de suma de un número real y otro complejo
c= 12.3 + 14j
print(c)
#13) Realizar una operación de multiplicación
print('El producto de 4 x 5 es igual a:',4*5)
#14) Mostrar el resultado de elevar 2 a la octava potencia
print('El resultado de elevar 2 a la octava potencia es igual a:',2**4)
#15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
a=27/4
print(a)
#16) De la división anterior solamente mostrar la parte entera
diventera=27//4
print('La parte entera de 27/4 es', diventera)
#17) De la división de 27 entre 4 mostrar solamente el resto
divresto = 27 % 4
print('El resto de la division 27/4 es:',divresto)
#18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
resultado=diventera*4+divresto
print(resultado)
#19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
cadena1="Hola"
cadena2="Mundo!!!!"
print(cadena1 + cadena2)
#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
#Porque un valor es de tipo cadena y el otro de tipo entero
"2"==2
#21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
x="2"
x=int(x)
x==2
#22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
#Porque no se puede convertir una variable tipo cadena a tipo flotante
a=float('3,8')
#23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
v=3
v-=1
print(v)
#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print(1<<2)

#25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

#26) Realizar una operación válida entre valores de tipo entero y string