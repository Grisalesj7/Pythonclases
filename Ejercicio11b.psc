Proceso Ejercicio11B_ContarNumerosPositivos
    Definir num, contador, total, i Como Entero
    contador <- 0
	
    Escribir "Ingrese la cantidad de números que va a introducir:"
    Leer total
	
    Para i <- 1 Hasta total Hacer
        Escribir "Ingrese un número:"
        Leer num
		
        Si num > 0 Entonces
            contador <- contador + 1
        FinSi
    FinPara
	
    Escribir "La cantidad de números positivos es: ", contador
FinProceso

