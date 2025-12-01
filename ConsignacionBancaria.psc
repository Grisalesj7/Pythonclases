Algoritmo ConsignacionBancaria
	Definir cuenta, cuentaValida Como Entero
	Definir monto, saldo Como Real
	
	cuentaValida <- 12345
	saldo <- 100000
	
	Escribir "Ingrese el número de cuenta:"
	Leer cuenta
	Escribir "Ingrese el monto a consignar:"
	Leer monto
	
	Si cuenta = cuentaValida Entonces
		Si monto > 0 Entonces
			saldo <- saldo + monto
			Escribir "Consignación exitosa."
			Escribir "Se consignaron: $", monto
			Escribir "Nuevo saldo: $", saldo
		Sino
			Escribir "? Monto inválido. Se devuelve: $", monto
		FinSi
	Sino
		Escribir "? Cuenta no existe. Se devuelve: $", monto
	FinSi
FinAlgoritmo

