Algoritmo descuento
	Definir precio, descuentot Como Real
	Definir cantidad Como Entero
	Escribir 'Digite el precio:'
	Leer precio
	Escribir 'Digite la cantidad:'
	Leer cantidad
	descuentot <- 0.10
	total_c = cantidad * precio
	descuentoenpesos = total_c * descuentot
	Si precio>100000 Entonces
		Escribir ' Tiene descuento, el total es: ', total_c - descuentoenpesos
		Escribir ' El descuento que se le dio a la compra es: ' descuentoenpesos
	SiNo
		Escribir ' No tiene descuento, el total es: ', total_c
	FinSi
FinAlgoritmo
