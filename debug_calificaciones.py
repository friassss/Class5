# ===== CONSTANTES =====
CALIF_MINIMA = 0
CALIF_MAXIMA = 100
CALIF_APROBATORIA = 70


# ===== FUNCIONES =====

def validar_calificacion(calif):
    # Devuelve True si la calificación está entre 0 y 100.
    if calif >= CALIF_MINIMA and calif <= CALIF_MAXIMA:
        return True
    else:
        return False


def calcular_promedio(calificaciones):
    # Suma todas las calificaciones y las divide entre cuántas hay.
    suma = 0
    for c in calificaciones:
        suma = suma + c
        promedio = suma / len(calificaciones)
    return promedio


def encontrar_mejor(calificaciones):
    # Devuelve la calificación más alta de la lista. 
    mejor = 0
    for c in calificaciones:
        if c > mejor:
            mejor = c
    return mejor


def obtener_letra(promedio):
    # Convierte el promedio numérico en una letra.
    if promedio >= 90:
        return "A"
    elif promedio >= 80:
        return "B"
    elif promedio >= 70:
        return "C"
    elif promedio >= 60:
        return "D"
    else:
        return "F"


def esta_aprobado(promedio):
    # Indica si aprobó según la calificación mínima aprobatoria.
    if promedio >= CALIF_APROBATORIA:
        return "APROBADO"
    else:
        return "REPROBADO"


# ===== PROGRAMA PRINCIPAL =====

print("=== REPORTE DE CALIFICACIONES ===")
nombre = input("Nombre del alumno: ")
num_materias = int(input("¿Cuántas materias cursó? "))

calificaciones = []
for i in range(num_materias):
    calif = int(input(f"Calificacion de la materia {i + 1}: "))
    if validar_calificacion(calif):
        calificaciones.append(calif)
    else:
        print("  -> Esa calificación no es válida (debe ser de 0 a 100)")

promedio = calcular_promedio(calificaciones)
mejor = encontrar_mejor(calificaciones)
letra = obtener_letra(promedio)
estado = esta_aprobado(promedio)

print("--------------------------------")
print("Alumno:   " + nombre)
print("Promedio: " + str(promedio))
print("Mejor:    " + str(mejor))
print("Letra:    " + letra)
print("Estado:   " + estado)