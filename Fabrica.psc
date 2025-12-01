Algoritmo Fabrica
	Definir pedido, nombre Como Cadena
	Definir cantidad, banco Como Entero
	Escribir 'Digite el nombre del cliente:'
	Leer nombre
	Escribir 'Digite su pedido:'
	Leer pedido
	Escribir 'Digite la cantidad que desea llevar:'
	Leer cantidad
	Escribir 'Digite la cantidad del banco'
	Leer banco
	total <- cantidad+banco
	Si banco>=10 Entonces
		Escribir ' Se realizo su pedido ', banco
	SiNo
		Escribir ' Rechazado por cartera vencida ', banco
	FinSi
FinAlgoritmo
