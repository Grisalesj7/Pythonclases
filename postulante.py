import math 

def calcular_nivel_postulante():
    print("--- CALCULADORA DE NIVEL DE CAPACITACIÓN ---")
    
    try:
        total_preguntas_str = input("Ingrese la cantidad total de preguntas realizadas: ")
        total_preguntas = int(total_preguntas_str)
        
        if total_preguntas <= 0:
            print("\n Error: El total de preguntas debe ser un número entero positivo.")
            return
            
    except ValueError:
        print("\n Error: Entrada inválida. Por favor, ingrese un número entero para el total de preguntas.")
        return
    
    try:
        respuestas_correctas_str = input("Ingrese la cantidad de respuestas CORRECTAS: ")
        respuestas_correctas = int(respuestas_correctas_str)
        
        if respuestas_correctas < 0:
            print("\n Error: Las respuestas correctas no pueden ser un número negativo.")
            return
            
        if respuestas_correctas > total_preguntas:
            print("\n Error: Las respuestas correctas no pueden exceder el total de preguntas.")
            return
            
    except ValueError:
        print("\n Error: Entrada inválida. Por favor, ingrese un número entero para las respuestas correctas.")
        return

    porcentaje = (respuestas_correctas / total_preguntas) * 100
    
    nivel = "" 

    if porcentaje >= 90:
        nivel = "Nivel Máximo"       
    elif porcentaje >= 75:
        nivel = "Nivel Medio"        
    elif porcentaje >= 50:
        nivel = "Nivel Regular"      
    else:
        nivel = "Fuera de Nivel"     
    
    print("\n" + "=" * 40)
    print(f"RESULTADOS DE LA EVALUACIÓN")
    print("=" * 40)
    print(f"Total de Preguntas: {total_preguntas}")
    print(f"Respuestas Correctas: {respuestas_correctas}")
    print(f" Porcentaje Obtenido: {porcentaje:.2f}%")
    print(f" Nivel de Capacitación: {nivel}")
    print("=" * 40)

calcular_nivel_postulante()