import sys # Importamos sys para salir del programa de forma limpia si se desea

fin = ""

while fin != 'f':
    
    try:
        edad = int(input("\nDigite la edad por favor: "))
    except ValueError:
        print("⚠️ Entrada no válida. Por favor, ingrese un número entero para la edad.")
        continue
    
    if edad <= 0:
        print("Edad no válida. Debe ser un número positivo.")
    elif edad <= 5:
        print("Infante")
    elif edad <= 10:
        print("Niño")
    elif edad <= 15:
        print("Pre-adolescente")
    elif edad <= 18:
        print("Adolescente")
    elif edad <= 25:
        print("Pre-adulto")
    elif edad <= 40:
        print("Adulto")
    elif edad <= 55:
        print("Pre-anciano")
    else:
        print("Anciano")
        
    print("-" * 30)
    fin = input("Digite (f) para finalizar el programa o presione Enter para continuar: ").strip().lower()
    
print("\nFin del programa. ¡Gracias!")

# Basicamente como esto aun no lo hemos visto, el sys sirve para manipular e inspeccionar el entorno 