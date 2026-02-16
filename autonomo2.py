# FASE 1: Inicialización
secreto = ["G", "A", "T", "O"]
oculto = ["_", "_", "_", "_"]
intentos_maximos = 6
errores = 0
letras_acertadas = 0

print("¡Bienvenido al juego del Ahorcado!")
print("Palabra: " + " ".join(oculto)) # Muestra: _ _ _ _

# FASE 2: El Ciclo Principal
# Nota: En Raptor el loop termina cuando esto es verdad. 
# En Python, el 'while' significa "mientras esto sea verdad, sigue repitiendo".
while errores < intentos_maximos and letras_acertadas < 4:
    
    # FASE 3: Pedir la letra
    # El .upper() convierte automáticamente lo que escribas a mayúscula
    letra_jugador = input("Adivina una letra: ").upper()
    hubo_acierto = 0
    
    # FASE 4: Comprobar la letra (El Loop Interno)
    # range(4) genera los números 0, 1, 2, 3 (los índices de nuestra palabra)
    for indice in range(4):
        if letra_jugador == secreto[indice]:
            # Solo sumamos acierto si esa posición aún tiene un guion bajo
            # (Esto evita que hagas trampa poniendo la 'A' 4 veces)
            if oculto[indice] == "_":
                oculto[indice] = letra_jugador
                hubo_acierto = 1
                letras_acertadas += 1
            else:
                hubo_acierto = 1 # Ya la habías adivinado, no te castigamos, pero no suma punto
                
    # FASE 5: Sumar errores y Mostrar progreso
    if hubo_acierto == 0:
        errores += 1
        print("❌ ¡Letra incorrecta!")
    else:
        print("✅ ¡Bien hecho!")
        
    # Mostrar el tablero actualizado. '.join' une la lista con espacios
    print("Palabra: " + " ".join(oculto))
    print("Te quedan " + str(intentos_maximos - errores) + " intentos.\n")

# FASE 6: Resultado Final (Fuera del ciclo)
if letras_acertadas == 4:
    print("🏆 ¡Felicidades! Has ganado. La palabra secreta era GATO.")
else:
    print("💀 Fin del juego. Te has ahorcado. La palabra secreta era GATO.")