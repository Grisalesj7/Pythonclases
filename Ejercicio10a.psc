Proceso Ejercicio10A_GastoSemanal
    Definir pasajes, refrigerio, totalDiario, totalSemanal Como Real
	
    Escribir "Ingrese el gasto diario en pasajes:"
    Leer pasajes
	
    Escribir "Ingrese el gasto diario en refrigerio:"
    Leer refrigerio
	
    totalDiario <- pasajes + refrigerio
    totalSemanal <- totalDiario * 6
	
    Escribir "El gasto total semanal (lunes a sábado) es: ", totalSemanal
FinProceso

