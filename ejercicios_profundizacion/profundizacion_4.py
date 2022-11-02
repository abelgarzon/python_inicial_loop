# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 3.0

# NOTA:
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realizar una calculadora
- Realizar un programa que se ejecute infinitas
  veces usando un bucle While True
- El programa se deberá terminar cuando el
  usuario indique la opción correspondiente
- Dentro del se debe ingresar por línea de comando dos números
- Luego se ingresará como tercera entrada al programa
  la operación que se desea ejecutar:
- 1- Suma (+)
- 2- Resta (-)
- 3- Multiplicación (*)
- 4- División (/)
- 5- SALIR

Se debe efectuar el cálculo correcto según la
operación ingresada por consola

Alumno:
- Comience por generar el bucle While True
- Dentro del bucle imprima con prints el menú
  de opciones en consola.

- Crear una una variable llamada numero_1
  para almacenar el primer número decimal que usted
  debe ingresar por consola con la función input

- Crear una una variable llamada numero_2
  para almacenar el primer número decimal que usted
  debe ingresar por consola con la función input

- Crear una una variable llamada operacion
  para almacenar la operación que se desea efectuar
  ingresada por consola con la función input

- Armar una serie de condicionales para evaluar
  que operación efectuar. Deberá guardar el resultado
  de la operación en una variable llamada resultado

- Si el usuario ingresa la operación de SALIR, deberá
  finalizar el bucle con la sentencia break.

- Si el usuario ingresa una opción fuera del rango
  solicitado de opciones, el programa no deberá
  estallar, no deberá hacer nada permitiendo
  que el bucle While vuelva a realizar la consulta
  en la próxima iteración.
'''

from os import system

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

def borrar_pantalla():
  system('cls')
  return

def reiniciar():
  input(mensaje_reiniciar)
  flag_error = True
  borrar_pantalla()
  return flag_error

borrar_pantalla()

mensaje_continuar = 'Pulsa enter para regresar al MENU:'
mensaje_reiniciar = 'Pulsa enter para REINICAR'

mensaje_error_1 = '''Error!!!
debes ingresar una opción entre 0 y 5'''

mensaje_error_2 = '''Error!!!
debes ingresar un número entero'''

while True:
#  flag_error es una bandera que indica un error en el ingreso de datos, si
#  cambia a True el programa correra sin procesar datos hasta regresar a MENU
  flag_error = False

  print("Mi Calculadora (^_^)")
  print('*** MENU DE OPCIONES ***\n1 - Suma(+)\n2 - Resta(-)')
  print('3 - Multiplicación(*)\n4 - División(/)\n5 - SALIR')

  operacion = input('Ingrese la opción: ')

#  Verificamos que la operación seleccionada sea un entero
#  Si es un entero verificamos que este en en el rango de 0 a 5
#  Si no esta en dicho rango, informamos al usuario y regresamos al MENU
#  Tambien verificamos que operacion no sea igual a 5 (SALIR), si es 5
#  salimos del programa
  try:
    operacion = int(operacion)
    if operacion <= 0 or operacion > 5:
      borrar_pantalla()
      print(mensaje_error_1)
      flag_error = reiniciar()
    elif operacion == 5:
      system('cls')
      break
  except:
    borrar_pantalla()
    print(mensaje_error_1)
    flag_error = reiniciar()

#  En esta parte solicitamos los operandos al usuario y verificamos
#  que sean números enteros, si no, regresamos al MENU

  if flag_error == False:
    numero_1 = input('Ingrese el primer número: ')
    try:
      numero_1 = int(numero_1)
    except:
      borrar_pantalla()
      print(mensaje_error_2)
      flag_error = reiniciar()

  if flag_error == False:
    numero_2 = (input('Ingrese el segundo número: '))
    try:
      numero_2 = int(numero_2)
    except:
      borrar_pantalla()
      print(mensaje_error_2)
      flag_error = reiniciar()

#  Verificamos la operación y la realizamos
  if flag_error == False:
    if operacion == 1:
      print(f'suma = {numero_1 + numero_2}')
    elif operacion == 2:
      print(f'resta = {numero_1 - numero_2}')
    elif operacion == 3:
      print(f'multiplicación = {numero_1 * numero_2}')
    elif operacion == 4: print(f'división = {(numero_1 / numero_2):.2f}')

    continuar = str(input(mensaje_continuar))
    borrar_pantalla()
