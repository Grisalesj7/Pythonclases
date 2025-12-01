Algoritmo Compra
	Definir Valorc, cantidad Como Real
	Definir producto Como Cadena
	descuento <- 0.10
	Escribir 'Bienvenido a la tienda'
	Escribir 'Digite el producto que desea llevar:'
	Leer producto
	Escribir 'Digite el valor del producto:'
	Leer Valorc
	Escribir 'Digite la cantidad que desea llevar de este producto:'
	Leer cantidad
	total <- descuento/Valorc
	Si Valorc>=100000 Entonces
		Escribir 'Se aplica descuento del 10%:', total
	SiNo
		Escribir 'No se aplica en este caso', total
	FinSi
FinAlgoritmo
