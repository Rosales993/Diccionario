estudiantes = {}

def agregar_estudiante(nombre, edad, calificaciones):

  estudiantes[nombre] = {'edad': edad, 'calificaciones': calificaciones}

def consultar_estudiante(nombre):

  if nombre in estudiantes:
    estudiante = estudiantes[nombre]
    print(f"Nombre: {nombre}")
    print(f"Edad: {estudiante['edad']}")
    print(f"Calificaciones: {estudiante['calificaciones']}")
  else:
    print(f"El estudiante {nombre} no existe.")

def calcular_promedio(nombre):

  if nombre in estudiantes:
    estudiante = estudiantes[nombre]
    promedio = sum(estudiante['calificaciones']) / len(estudiante['calificaciones'])
    print(f"El promedio de {nombre} es: {promedio:.2f}")
  else:
    print(f"El estudiante {nombre} no existe.")

# Se agregan estudiantes
agregar_estudiante("Jose", 20, [9, 8, 7, 10])
agregar_estudiante("Rosales", 22, [10, 9, 9, 8])
agregar_estudiante("David",21,[10,10,10,10])
agregar_estudiante("Chavez",23,[7,10,5,9])

#Registro de Diccionario
print(estudiantes)

# Consultar información de un estudiante
consultar_estudiante("Chavez")
# Calcular el promedio de un estudiante
calcular_promedio("Chavez")


