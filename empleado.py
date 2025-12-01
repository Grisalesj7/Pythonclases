def calcular_salario_empleado_interactivo():
    
    print("--- 💸 INGRESO DE DATOS DEL TRABAJADOR ---")
    
    try:
        salario_minimo = float(input("Ingrese el Salario Mínimo Mensual Legal Vigente (SMMLV) [Ej. 1300000]: "))
        auxilio_transporte = float(input("Ingrese el valor del Auxilio de Transporte [Ej. 162000]: "))
        
        print("\n--- Horas y Tarifas ---")
        horas_semanales_base = float(input("Horas trabajadas a la semana (Base 48): "))
        valor_hora_base = float(input("Valor de la hora base: "))
        horas_extras_diurnas_semana = float(input("Horas Extras Diurnas a la semana: "))
        
        print("\n--- Deducciones Fijas y Variables ---")
        deduccion_fondo_empleados = float(input("Deducción fija para Fondo de Empleados: "))
        demanda_alimentos_fija = float(input("Deducción fija por Demanda de Alimentos (Si aplica, sino 0): "))
        umbral_retencion_alimentos = 3740000
        
        porcentaje_emi = 0.03
        porcentaje_funeraria = 0.02
        porcentaje_demanda_alimentos_alto = 0.30
        recargo_extra_diurna = 0.25
        
    except ValueError:
        print("\nError: Por favor, ingrese solo números para los valores solicitados.")
        return

    horas_mes_base = horas_semanales_base * (52 / 12) 
    salario_base_mensual = horas_mes_base * valor_hora_base
    
    horas_extras_diurnas_mes = horas_extras_diurnas_semana * (52 / 12)
    valor_hora_extra_diurna = valor_hora_base * (1 + recargo_extra_diurna)
    valor_horas_extras = horas_extras_diurnas_mes * valor_hora_extra_diurna
        
    salario_bruto_mensual = round(salario_base_mensual + valor_horas_extras)
    
    salario_minimo_doble = 2 * salario_minimo
    valor_auxilio_transporte = 0
    if salario_bruto_mensual <= salario_minimo_doble:
        valor_auxilio_transporte = auxilio_transporte
        
    deduccion_emi = salario_bruto_mensual * porcentaje_emi
    deduccion_funeraria = salario_bruto_mensual * porcentaje_funeraria
    
    retencion_demanda_alimentos_condicional = 0
    if salario_bruto_mensual > umbral_retencion_alimentos:
        retencion_demanda_alimentos_condicional = salario_bruto_mensual * porcentaje_demanda_alimentos_alto
    
    deducciones_totales = round(
        deduccion_emi +
        deduccion_funeraria +
        deduccion_fondo_empleados +
        demanda_alimentos_fija +
        retencion_demanda_alimentos_condicional
    )
    
    salario_neto_a_pagar = round(
        salario_bruto_mensual +
        valor_auxilio_transporte -
        deducciones_totales
    )

    print("\n" + "=" * 40)
    print("      RESUMEN DE LIQUIDACIÓN MENSUAL")
    print("=" * 40)
    
    print(f"Salario Bruto Mensual (Base + Extras): ${salario_bruto_mensual:,.0f}")
    print(f"Auxilio de Transporte:                 ${valor_auxilio_transporte:,.0f}")
    print("-" * 40)

    print("### DETALLE DE DEDUCCIONES ###")
    print(f"1. EMI (3%):                           ${round(deduccion_emi):,.0f}")
    print(f"2. Funeraria (2%):                     ${round(deduccion_funeraria):,.0f}")
    print(f"3. Fondo de Empleados:                 ${deduccion_fondo_empleados:,.0f}")
    print(f"4. Demanda de Alimentos (Fija):        ${demanda_alimentos_fija:,.0f}")
    print(f"5. Retención Alimentos (> $3.74M):     ${round(retencion_demanda_alimentos_condicional):,.0f}")
    print("-" * 40)

    print(f"Total Deducciones:                     ${deducciones_totales:,.0f}")
    print("=" * 40)
    print(f"**SALARIO NETO A PAGAR:** **${salario_neto_a_pagar:,.0f}**")
    print("=" * 40)


if __name__ == "__main__":
    calcular_salario_empleado_interactivo()