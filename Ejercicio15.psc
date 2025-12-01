Proceso Ejercicio15_ControlEntradaEvento
    Definir edad, mayores, menores Como Entero
    mayores <- 0
    menores <- 0
	
    Escribir "=== Control de entrada al evento ==="
    Escribir "Ingrese la edad del asistente (0 para finalizar):"
    Leer edad
	
    Mientras edad <> 0 Hacer
        Si edad >= 18 Entonces
            Escribir "Puede ingresar al evento."
            mayores <- mayores + 1
        Sino
            Escribir "No puede ingresar al evento (menor de edad)."
            menores <- menores + 1
        FinSi
		
        Escribir ""
        Escribir "Ingrese la edad del siguiente asistente (0 para finalizar):"
        Leer edad
    FinMientras
	
    Escribir "Total de mayores de edad: ", mayores
    Escribir "Total de menores de edad: ", menores
FinProceso

