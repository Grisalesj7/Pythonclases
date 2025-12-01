Algoritmo Aprendiznota
	Definir nota1, nota2, nota3, nota4 Como Real
	Escribir 'Digite el nombre del aprendiz:'
	Leer Aprendiz
	Escribir 'Digite la nota1:'
	Leer nota1
	Escribir 'Digite la nota2:'
	Leer nota2
	Escribir 'Digite la nota 3'
	Leer nota3
	Escribir 'Digite la nota4'
	Leer nota4
	promedio <- 3.5
	total <- nota1+nota2+nota3+nota4/promedio
	promedio <- total
	Si promedio>=3.5 Entonces
		Escribir 'Aprobado', total
	SiNo
		promedio <- 0
		Escribir ' No aprobado ', total, ' Debes hacer plan de mejoramiento '
	FinSi
FinAlgoritmo
