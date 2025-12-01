Proceso Ejercicio14_SalarioSemanal
    Definir horasTrabajadas, valorHora, salario, extra Como Real
	
    Escribir "Ingrese las horas trabajadas en la semana:"
    Leer horasTrabajadas
	
    Escribir "Ingrese el valor por hora:"
    Leer valorHora
	
    salario <- horasTrabajadas * valorHora
	
    Si horasTrabajadas > 40 Entonces
        extra <- (horasTrabajadas - 40) * valorHora * 0.5
        salario <- salario + extra
    FinSi
	
    Escribir "Salario total: ", salario
FinProceso

