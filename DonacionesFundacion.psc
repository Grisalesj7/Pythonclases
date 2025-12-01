Algoritmo DonacionesFundacion
	Definir tipo Como Caracter
	Definir monto, total Como Real
	Definir contE, contO, n, i Como Entero
	
	contE <- 0
	contO <- 0
	total <- 0
	
	Escribir "¿Cuántas donaciones se registraron hoy?"
	Leer n
	
	Para i <- 1 Hasta n Hacer
		Escribir "Ingrese tipo de donación (E=Efectivo / O=Obra social):"
		Leer tipo
		Escribir "Ingrese el monto donado:"
		Leer monto
		
		total <- total + monto
		
		Si tipo = "E" O tipo = "e" Entonces
			contE <- contE + 1
		Sino
			Si tipo = "O" O tipo = "o" Entonces
				contO <- contO + 1
			FinSi
		FinSi
	FinPara
	
	Escribir "=== RESULTADOS DEL DÍA ==="
	Escribir "Donaciones en efectivo: ", contE
	Escribir "Donaciones por obra social: ", contO
	Escribir "Total ingresado en caja: $", total
FinAlgoritmo

