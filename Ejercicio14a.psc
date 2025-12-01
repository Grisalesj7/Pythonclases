Proceso Ejercicio14A_SalarioSemanalPorDia
    Definir horas, valorHora, totalSemanal, salarioDia, i Como Real
    totalSemanal <- 0
	
    Para i <- 1 Hasta 5 Hacer
        Escribir "Día ", i
		
        Escribir "Ingrese las horas trabajadas:"
        Leer horas
		
        Escribir "Ingrese el valor por hora:"
        Leer valorHora
		
        salarioDia <- horas * valorHora
		
        Si horas > 8 Entonces
            salarioDia <- salarioDia + ((horas - 8) * valorHora * 0.5)
        FinSi
		
        totalSemanal <- totalSemanal + salarioDia
		
        Escribir "Salario del día ", i, ": ", salarioDia
    FinPara
	
    Escribir "El salario total semanal es: ", totalSemanal
FinProceso

