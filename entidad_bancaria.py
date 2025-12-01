import datetime

def generar_ticket():

    id_sucursal = "Sucursal Central 101"
    ticket_generado = False
    servicio = ""
    consecutivo_ticket = ""
    
    while True:
        print("=" * 45)
        print("      Bienvenido al Dispensador de Tickets   ")
        print("=" * 45)
        
        respuesta_inicial = input("¿Desea iniciar la transacción? (S/N): ").strip().upper()
        
        if respuesta_inicial == 'N':
            print("Transacción cancelada. ¡Gracias por su visita!")
            return 
        
        elif respuesta_inicial == 'S':
            break 
        
        else:
            print("Opción no válida. Por favor, ingrese S para Sí o N para No.")

    print("-" * 45)
    print("--- Ingreso de Datos ---")
    nombre_usuario = input("Por favor, ingrese su nombre completo: ").strip()
    cedula_usuario = input("Por favor, ingrese su número de cédula: ").strip()
    
    while True:
        print("-" * 45)
        print("--- Menú de Opciones Disponibles ---")
        print("1. Servicio de **Caja**")
        print("2. Servicio al **Cliente**")
        print("3. Pago de **Impuestos**")
        print("4. **Crédito Hipotecario**")
        print("5. Operaciones con **Tarjeta de Crédito**")
        print("-" * 45)
        
        try:
            opcion_servicio = int(input("Ingrese el número de la opción deseada (1-5): "))
            if 1 <= opcion_servicio <= 5:
                break
            else:
                print("¡Opción fuera de rango! Por favor, ingrese un número del 1 al 5.")
        except ValueError:
            print("¡Entrada no válida! Por favor, ingrese un número.")

    match opcion_servicio:
        case 1:
            servicio = "Servicio de Caja"
            consecutivo_ticket = "CAJ-001"
            ticket_generado = True
        case 2:
            servicio = "Servicio al Cliente"
            consecutivo_ticket = "CLI-005"
            ticket_generado = True
        case 3:
            servicio = "Pago de Impuestos"
            consecutivo_ticket = "IMP-002"
            ticket_generado = True
        case 4:
            servicio = "Crédito Hipotecario"
            consecutivo_ticket = "HIP-003"
            ticket_generado = True
        case 5:
            servicio = "Tarjeta de Crédito"
            consecutivo_ticket = "TDC-004"
            ticket_generado = True
        case _: 
            print("¡ERROR! Opción inválida. No se generará ticket.")
            ticket_generado = False

    print("-" * 45)
    if ticket_generado:
        fecha_actual = datetime.date.today().strftime("%d/%m/%Y")
        
        print("TICKET GENERADO")
        print("=" * 45)
        print(f"| ID Sucursal: {id_sucursal:<29}|")
        print(f"| Servicio: {servicio:<32}|")
        print("|" + "-" * 43 + "|")
        print(f"| TICKET N°: {consecutivo_ticket:<31}|")
        print("|" + "-" * 43 + "|")
        print(f"| Usuario: {nombre_usuario:<33}|")
        print(f"| Cédula: {cedula_usuario:<34}|")
        print(f"| Fecha: {fecha_actual:<35}|")
        print("=" * 45)
        print(f"Por favor, diríjase al área de **{servicio}**.")
    else:
        print("El sistema no pudo generar su ticket debido a una opción inválida.")
        
    print("-" * 45)
    
if __name__ == "__main__":
    generar_ticket()


    # Cabe recalcar que los print que tienen asterisco y esto (*45), sirve para crear un borde ya sea superior o inferior
    # El strip basicamente sirve para limpiar la entrada del usuario