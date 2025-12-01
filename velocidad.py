try:
    velocidad = float(input("Por favor, digita la velocidad actual (en km/h): "))

    if velocidad > 100:
        print(f"ERROR: Tu velocidad ({velocidad:.1f} km/h) excede el límite MÁXIMO (100 km/h). ¡Disminuye la velocidad!")
    elif velocidad > 80:
        print(f"Estás en la ruta nacional (Límite: 100 km/h). Tu velocidad es: **{velocidad:.1f} km/h**.")
    elif velocidad > 60:
        print(f"Estás en la vía rural (Límite: 80 km/h). Tu velocidad es: **{velocidad:.1f} km/h**.")
    elif velocidad > 30:
        print(f"Estás en la vía urbana (Límite: 60 km/h). Tu velocidad es: **{velocidad:.1f} km/h**.")
    elif velocidad > 0:
        print(f"¡Cuidado! Estás en la zona escolar (Límite: 30 km/h). Tu velocidad es: **{velocidad:.1f} km/h**.")
    elif velocidad == 0:
        print("El vehículo está detenido.")
    else:
        print("El valor ingresado no es válido para la velocidad.")

except ValueError:
    print("Entrada no válida. Por favor, ingresa solo números (enteros o decimales) para la velocidad.")

    
    