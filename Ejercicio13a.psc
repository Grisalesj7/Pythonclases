Proceso Ejercicio13A_PromedioCincoEstudiantes
    Definir nota1, nota2, nota3, prom Como Real
    Definir i Como Entero
	
    Para i <- 1 Hasta 5 Hacer
        Escribir "Estudiante ", i
		
        Escribir "Ingrese la primera nota:"
        Leer nota1
		
        Escribir "Ingrese la segunda nota:"
        Leer nota2
		
        Escribir "Ingrese la tercera nota:"
        Leer nota3
		
        prom <- (nota1 + nota2 + nota3) / 3
		
        Si prom >= 3.0 Entonces
            Escribir "Aprobó con: ", prom
        Sino
            Escribir "Reprobó con: ", prom
        FinSi
    FinPara
FinProceso

