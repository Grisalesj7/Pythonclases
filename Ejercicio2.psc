Proceso Ejercicio2
	Definir numero1 Como Entero
	Definir es_par Como Logico
	
	Escribir "Digite el numero: "
	Leer numero1
	
	Si (numero1 % 2 == 0) Entonces
		es_par = Verdadero
	SiNo
		es_par = Falso
	FinSi
	
	Si (es_par) Entonces
		Escribir " El numero: ", numero1 , " es par "
	SiNo
		Escribir " El numero: ", numero1 , " es impar "
	FinSi
FinProceso
