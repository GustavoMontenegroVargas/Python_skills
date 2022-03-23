 #Defina una función que halle TODOS los valores de las posiciones de un caracter específico dentro de una cadena de texto.

#-----------------------------
#Esta es la definición de la función.
#Esta función regresa una lista.
#Esta función es posible debido a que las cadenas de texto son iterables. 
# La búsqueda de caracteres es sensitive case

def Buscar_posición(text,character):
  numbers = []
  for i in range(len(text)):
    if text[i] == character:
      numbers.append(i)
  return numbers


#----------------------------
#Aquí ingresamos los valores en el argumento de la función.
print("Este mini-programa encuentra todos los valores de las posiciones de un caracter en específico dentro de una cadena de texto.")
print("\n")
texto = input("¿Qué texto usarás?: ")
caracter = input("¿Qué caracter quieres buscar?: ")


A = Buscar_posición(texto,caracter)
#----------------------------
#Esta es la ejecución en pantalla. 

print(f"{A} -> Estos son los valores de las posiciones donde se encuentra el caracter '{caracter}' en el texto '{texto}'")

print("\n")

#------------------------------
#Esta es la comprobación de la función.
print("Así demostramos, de una manera sencilla, que funciona")
for i in A:
  print(texto[i])


