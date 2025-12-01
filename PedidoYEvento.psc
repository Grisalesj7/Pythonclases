
	
Algoritmo PedidoYEvento
	Definir estado Como Caracter
	
	Escribir "¿El cliente está activo? (S = Sí / N = No):"
	Leer estado
	
	Si estado = "S" O estado = "s" Entonces
		Escribir "? Pedido aceptado."
	Sino
		Escribir "? Rechazado por cartera vencida."
	FinSi
	
	Definir edad, mayor, menor Como Entero
	Definir sexo Como Caracter
	Definir contH, contM, n, i Como Entero
	
	contH <- 0
	contM <- 0
	mayor <- 0
	menor <- 9999
	
	Escribir ""
	Escribir "=== REGISTRO DE VISITANTES AL EVENTO ==="
	Escribir "¿Cuántas personas ingresarán?"
	Leer n
	
	Para i <- 1 Hasta n Hacer
		Escribir "Ingrese sexo (M = Mujer / H = Hombre):"
		Leer sexo
		Escribir "Ingrese edad:"
		Leer edad
		
		Si sexo = "H" O sexo = "h" Entonces
			contH <- contH + 1
		Sino
			Si sexo = "M" O sexo = "m" Entonces
				contM <- contM + 1
			FinSi
		FinSi
		
		Si edad > mayor Entonces
			mayor <- edad
		FinSi
		Si edad < menor Entonces
			menor <- edad
		FinSi
	FinPara
	
	Escribir ""
	Escribir "=== RESULTADOS DEL EVENTO ==="
	Escribir "Cantidad de hombres: ", contH
	Escribir "Cantidad de mujeres: ", contM
	Escribir "Mayor edad registrada: ", mayor
	Escribir "Menor edad registrada: ", menor
FinAlgoritmo

