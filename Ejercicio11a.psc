Proceso Ejercicio11A_SumarNumerosHastaCero
    Definir num, suma Como Real
    suma <- 0
	
    Escribir "=== Suma de números (ingrese 0 para terminar) ==="
	
    Escribir "Ingrese un número:"
    Leer num
	
    Mientras num <> 0 Hacer
        suma <- suma + num
        Escribir "Ingrese otro número (0 para finalizar):"
        Leer num
    FinMientras
	
    Escribir "La suma total de los números ingresados es: ", suma
FinProceso

