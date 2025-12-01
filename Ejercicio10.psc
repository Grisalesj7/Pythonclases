Proceso Ejercicio10_CalcularDescuentoCompra
    Definir valorCompra, descuento, valorFinal Como Real
	
    Escribir "Ingrese el valor de la compra:"
    Leer valorCompra
	
    Si valorCompra > 100000 Entonces
        descuento <- valorCompra * 0.1
    Sino
        descuento <- 0
    FinSi
	
    valorFinal <- valorCompra - descuento
	
    Escribir "Valor a pagar: ", valorFinal
FinProceso

