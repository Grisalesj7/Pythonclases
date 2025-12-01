Proceso Ejercicio13_ContarPositivosNegativos
    Definir num, positivos, negativos, i Como Entero
    positivos <- 0
    negativos <- 0
	
    Para i <- 1 Hasta 5 Hacer
        Escribir "Ingrese un número:"
        Leer num
		
        Si num >= 0 Entonces
            positivos <- positivos + 1
        Sino
            negativos <- negativos + 1
        FinSi
    FinPara
	
    Escribir "Positivos: ", positivos, "  Negativos: ", negativos
FinProceso

