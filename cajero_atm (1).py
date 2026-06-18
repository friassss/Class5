# =============================================================================
#  CAJERO ATM POR CONSOLA  ·  Sesion 09 "Los muchos caminos"
#  Fundamentos de Programacion · UNITEC Atizapan · Ciclo 26-3
#  Profesor: Carlos Daniel Vaca Ramirez
# -----------------------------------------------------------------------------
#  El PLANO. Este archivo solo trae comentarios numerados (# PASO N).
#  Tu trabajo: leer cada instruccion y escribir tu codigo en el espacio en
#  blanco que sigue. NO borres los comentarios. Corre el programa despues de
#  cada paso para asegurarte de que no truena antes de continuar.
#
#  Objetivo: un cajero con MENU de al menos 4 opciones (consultar saldo,
#  depositar, retirar, salir) y validaciones construidas con DECISIONES
#  ANIDADAS y CONDICIONES COMPUESTAS (and, or, not).
# =============================================================================


# -----------------------------------------------------------------------------
# PASO 1: Crea las CONSTANTES del cajero (MAYUSCULAS, como en la sesion 6).
#   SALDO_INICIAL   -> con cuanto dinero arranca la cuenta, p. ej. 5000.0
#   RETIRO_MAXIMO   -> tope por operacion, p. ej. 9000.0
#   PIN_CORRECTO    -> un PIN de 4 digitos como texto, p. ej. "1234"
# -----------------------------------------------------------------------------

SALDO_INICIAL = 20000.0
RETIRO_MAXIMO = 5000.0
PIN_CORRECTO = 5822
COMISION = 0.015

# -----------------------------------------------------------------------------
# PASO 2: Define una variable 'saldo' que valga SALDO_INICIAL.
#   Sera el dinero disponible; cambiara con cada deposito o retiro.
# -----------------------------------------------------------------------------

saldo = SALDO_INICIAL

# -----------------------------------------------------------------------------
# PASO 3: VALIDACION DE ACCESO con una DECISION ANIDADA.
#   Pide el PIN con input(). Da hasta 3 intentos usando un for.
#   Dentro del for, anida un if:
#       si el pin escrito == PIN_CORRECTO -> avisa "Acceso concedido",
#           guarda acceso = True y rompe el ciclo con break.
#       si no -> avisa cuantos intentos quedan.
#   Si se agotan los 3 intentos sin acertar, acceso = False.
# -----------------------------------------------------------------------------

import time

while True:
    acceso = False

    for i in range(2,-1,-1):
        pin = input("Ingresa el PIN: ")

        if pin.isdigit():
            pin = int(pin)

            if pin == PIN_CORRECTO:
                print("Acceso concedido") 
                acceso = True
                break

            else:
                print(f"Número de intentos restantes: {i}")

        else:
            print("El PIN solo debe contener números.")
            print(f"Número de intentos restantes: {i}")

# -----------------------------------------------------------------------------
# PASO 4: Si NO hubo acceso (usa 'not acceso' o 'acceso == False'),
#   muestra "Tarjeta retenida" y termina el programa.
#   Pista: puedes usar la condicion compuesta para tomar la decision.
# -----------------------------------------------------------------------------

    if acceso:
        break

    if not acceso:
        print("Tarjeta retenida por 1 minuto")
        time.sleep(60)
        print("Bloqueo finalizado. Puede intentarlo nuevamente")
    exit

# -----------------------------------------------------------------------------
# PASO 5: EL MENU. Repite con un while True para que el cajero siga vivo
#   hasta que el usuario decida salir. Imprime las 4 opciones:
#       1) Consultar saldo
#       2) Depositar
#       3) Retirar
#       4) Salir
#   Luego pide la opcion con input() y guardala en 'opcion'.
# -----------------------------------------------------------------------------

print("")
print("==========Cajero ATM==========")
print("1) Consultar saldo")
print("2) Depositar")
print("3) Retirar")
print("4) Salir")
print("5) Ver movimientos")

historial = []

while True:
    
    print("")
    opcion = str(input("Elige una opción: "))

# -----------------------------------------------------------------------------
# PASO 6: OPCION 1 - Consultar saldo.
#   Dentro del while, con un if opcion == "1": imprime el saldo con formato,
#   p. ej.  print(f"Tu saldo es ${saldo:.2f}")
# -----------------------------------------------------------------------------

    match opcion:
        case "1":
            print(f"Tu saldo es ${saldo:.2f}")
            historial.append("Consulta de saldo")

# -----------------------------------------------------------------------------
# PASO 7: OPCION 2 - Depositar (con VALIDACION ANIDADA).
#   elif opcion == "2":
#       pide el monto y conviertelo con float(...).
#       if monto > 0:           # condicion: el deposito debe ser positivo
#           suma el monto al saldo e informa el nuevo saldo.
#       else:
#           avisa "Monto invalido".
#   Tip: protege el float() con try/except por si escriben texto.
# -----------------------------------------------------------------------------

        case "2":
            while True:
                try:
                    monto = float(input("¿Qué monto va a depositar? "))
                    if monto > 0:
                        saldo += monto
                        print(f"Tu nuevo saldo es de ${saldo}")
                        historial.append(f"Depósito: + ${monto}")
                    else:
                        print("Monto inválido.")
                    break
                except ValueError:
                    print("Debes ingresar un monto válido.")

# -----------------------------------------------------------------------------
# PASO 8: OPCION 3 - Retirar (DECISIONES ANIDADAS + LOGICA COMPUESTA).
#   elif opcion == "3":
#       pide el monto y conviertelo con float(...).
#       if monto <= 0:
#           "Monto invalido".
#       elif monto > RETIRO_MAXIMO:
#           "Excede el retiro maximo por operacion".
#       elif monto > saldo:
#           "Fondos insuficientes".
#       else:
#           resta el monto al saldo y entrega el dinero.
#   Reto: ¿puedes juntar dos reglas con 'and' u 'or' para acortar el if?
# -----------------------------------------------------------------------------

        case "3":
            while True:
                try:
                    monto = float(input("¿Qué monto va a retirar? "))
                    if monto <= 0:
                        print("Monto invalido.")
                    elif monto > RETIRO_MAXIMO:
                        print("Excede el retiro maximo por operacion.")
                        historial.append(f"Retiro rechazado de ${monto}")
                    elif monto > saldo:
                        print("Fondos insuficientes.")
                        historial.append(f"Retiro rechazado de ${monto}")
                    else:
                        if monto >= 500:
                            print("Se te cobrará una comisión del 1.5% por tu retiro.")
                            monto_com = monto * COMISION
                            monto += monto_com
                            print(f"El nuevo monto es de {monto}.")
                        else:
                            print("Retiro mínimo, no se te cobrará comisión.")
                        saldo -= monto
                        print(f"Tu nuevo saldo es de ${saldo}")
                        historial.append(f"Retiro: - ${monto}")
                    break
                except ValueError:
                    print("Debes ingresar un monto válido.")

# -----------------------------------------------------------------------------
# PASO 9: OPCION 4 - Salir.
#   elif opcion == "4":
#       despidete y rompe el ciclo con break.
# -----------------------------------------------------------------------------

        case "4":
            print("Gracias por usar el Cajero ATM!")
            break

# -----------------------------------------------------------------------------
# PASO 10: OPCION invalida.
#   else:
#       avisa "Opcion no valida, intenta de nuevo".
#   Con esto el menu queda blindado: cualquier tecla equivocada no rompe nada.
# -----------------------------------------------------------------------------

        case "5":
            print("====== HISTORIAL ======")
            if len(historial) == 0:
                print("No hay movimientos registrados.")
            else:
                for movimiento in historial:
                    print(movimiento)

        case _:
            print ("Opción inválida, intenta de nuevo")

# =============================================================================
#  EJEMPLO DE CORRIDA (asi se debe ver tu cajero terminado)
# -----------------------------------------------------------------------------
#   Ingresa tu PIN: 0000
#   PIN incorrecto. Te quedan 2 intentos.
#   Ingresa tu PIN: 1234
#   Acceso concedido. Bienvenido.
#
#   ===== CAJERO ATM =====
#   1) Consultar saldo
#   2) Depositar
#   3) Retirar
#   4) Salir
#   Elige una opcion: 1
#   Tu saldo es $5000.00
#
#   Elige una opcion: 3
#   ¿Cuanto deseas retirar? 12000
#   Excede el retiro maximo por operacion ($9000.00).
#
#   Elige una opcion: 3
#   ¿Cuanto deseas retirar? 2000
#   Entrega de $2000.00. Tu nuevo saldo es $3000.00
#
#   Elige una opcion: 4
#   Gracias por usar el cajero. Hasta pronto.
# =============================================================================


# =============================================================================
#  RETOS EXTRA (opcionales · suman puntos de actividad)
# -----------------------------------------------------------------------------
#  A. VERSION CON match-case: refactoriza el menu (PASOS 6 a 10) usando
#     match opcion:
#         case "1": ...
#         case "2": ...
#         case "3": ...
#         case "4": ...
#         case _:  ...   # el comodin, equivale al "else"
#     Compara: ¿quedo mas legible que el if-elif-else? Anota tu conclusion.
#
#  B. Cobra una COMISION del 1.5% en cada retiro usando una constante
#     COMISION = 0.015 y una condicion compuesta para no cobrarla si el
#     retiro es menor a $500 (clientes pequenos no pagan).
#
#  C. Lleva un HISTORIAL: guarda cada operacion en una lista y agrega una
#     5a opcion "Ver movimientos" que la imprima.
#
#  D. Tras 3 PIN incorrectos, en vez de terminar, bloquea la tarjeta por
#     "tiempo" mostrando una cuenta regresiva con time.sleep().
# =============================================================================
