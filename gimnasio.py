import datetime

# --- Variables Globales para el seguimiento del día ---
clientes_registrados = 0
ingresos_totales = 0.0
IVA_PERCENTAGE = 0.19  # 19% de IVA (ejemplo)

# Sedes disponibles
SEDES_GIMNASIO = ["Robledo", "Bello", "Estadio"]

# Diccionarios para el Análisis Administrativo Detallado
ingresos_por_plan = {"Basico": 0.0, "Plata": 0.0, "Oro": 0.0}
ingresos_por_pago = {"Transferencia": 0.0, "Tarjeta": 0.0}
# Nuevo diccionario para el desglose por Sede
ingresos_por_sede = {sede: 0.0 for sede in SEDES_GIMNASIO} # Inicializa las sedes a 0.0

# --- Funciones Auxiliares ---

def calcular_imc(peso, estatura):
    """Calcula el Índice de Masa Corporal (IMC)."""
    if estatura > 0:
        return round(peso / (estatura ** 2), 2)
    return 0.0

def obtener_diagnostico_y_recomendacion(imc):
    """Determina el diagnóstico y la recomendación según la tabla de IMC."""
    # (La lógica del diagnóstico y la recomendación se mantiene igual)
    if imc < 16.00:
        return ("Delgadez Severa", "Su peso es demasiado bajo - Consulte su médico.")
    elif 16.00 <= imc <= 16.99:
        return ("Delgadez Moderada", "Su peso es bajo - Incluya calorías y carbohidratos en su dieta.")
    elif 17.00 <= imc <= 18.49:
        return ("Delgadez Leve", "Su peso es ligeramente bajo - Mejore sus hábitos alimenticios.")
    elif 18.50 <= imc <= 24.99:
        return ("Normal", "Usted tiene un peso saludable.")
    elif 25.00 <= imc <= 29.99:
        return ("Preobeso", "Su peso es levemente alto - Procure hacer ejercicio.")
    elif 30.00 <= imc <= 34.99:
        return ("Obesidad Leve", "Su peso es alto - Controle su dieta y realice ejercicio.")
    elif 35.00 <= imc <= 39.99:
        return ("Obesidad Media", "Su peso es muy alto - Visite a su médico y controle su dieta.")
    else:
        return ("Obesidad Mórbida", "Su peso es excesivamente alto - Visite a su médico cuanto antes.")

def asignar_rutina_inicial(diagnostico):
    """Asigna una rutina inicial basada en el diagnóstico de IMC."""
    if "Delgadez" in diagnostico:
        return "Fuerza y Volumen (Bajo Impacto). Objetivo: Ganancia de Masa Muscular."
    elif diagnostico == "Normal" or diagnostico == "Preobeso":
        return "Entrenamiento Funcional Equilibrado. Objetivo: Mantenimiento y Acondicionamiento."
    elif "Obesidad" in diagnostico:
        return "Cardio y Resistencia (Prioridad Articular). Objetivo: Quema Calórica Progresiva."
    else:
        return "Evaluación Personalizada por el Entrenador."

def calcular_tmb(peso, estatura, edad, sexo):
    """Calcula la Tasa Metabólica Basal (TMB) usando la fórmula de Mifflin-St Jeor."""
    estatura_cm = estatura * 100
    if sexo.lower() == 'mujer':
        tmb = (10 * peso) + (6.25 * estatura_cm) - (5 * edad) - 161
    elif sexo.lower() == 'hombre':
        tmb = (10 * peso) + (6.25 * estatura_cm) - (5 * edad) + 5
    else:
        return 0
    return round(tmb)

def calcular_costo_y_iva(plan_seleccionado, modalidad_pago):
    """Calcula el valor base, los descuentos, el IVA y el costo total."""
    PLANES = {
        "Basico": 60000,
        "Plata": 85000,
        "Oro": 100000
    }

    valor_base = PLANES.get(plan_seleccionado, 0)
    descuento_pago = 0.0

    # Descuentos según el Plan Oro y la Modalidad de Pago
    if plan_seleccionado == "Oro":
        if modalidad_pago == "Transferencia":
            descuento_pago = 0.10
        elif modalidad_pago == "Tarjeta":
            descuento_pago = 0.05
    
    valor_con_descuento_pago = valor_base * (1 - descuento_pago)

    # Simulación de pronto pago
    pago_a_tiempo = input("¿El pago se realiza dentro de los tres primeros días del mes? (si/no): ").lower() == 'si'
    
    descuento_pronto_pago = 0.0
    if pago_a_tiempo:
        descuento_pronto_pago = 0.01
    
    valor_final_sin_iva = valor_con_descuento_pago * (1 - descuento_pronto_pago)
    
    # Cálculo del IVA y el Costo Total
    valor_iva = valor_final_sin_iva * IVA_PERCENTAGE
    costo_total = valor_final_sin_iva + valor_iva

    return valor_iva, costo_total, valor_base

# --- Lógica Principal del Algoritmo ---

print("--- 🏋️ Sistema de Registro de Clientes del Gimnasio V3.0 (Con Sedes) ---")

# Ciclo principal para atender a los clientes
while True:
    print("\n--- Registro de Nuevo Cliente ---")
    
    # 1. Solicitar datos del cliente y Sede
    try:
        nombres = input("Nombres: ")
        edad = int(input("Edad: "))
        documento = input("Documento: ")
        eps = input("EPS: ")
        correo = input("Correo electrónico: ")
        
        while True:
            sexo = input("Sexo (Hombre/Mujer): ").lower()
            if sexo in ['hombre', 'mujer']:
                break
            print("❌ Error: Ingrese 'Hombre' o 'Mujer'.")
        
        # --- NUEVA FUNCIÓN: SELECCIÓN DE SEDE ---
        print("\n--- Sedes Disponibles ---")
        for i, sede in enumerate(SEDES_GIMNASIO):
            print(f"{i + 1}. {sede}")
            
        while True:
            try:
                sede_opcion = int(input(f"Seleccione el número de la sede (1-{len(SEDES_GIMNASIO)}): "))
                if 1 <= sede_opcion <= len(SEDES_GIMNASIO):
                    sede_seleccionada = SEDES_GIMNASIO[sede_opcion - 1]
                    break
                else:
                    print("Selección de sede inválida.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        peso = float(input("Peso (kg): "))
        estatura = float(input("Estatura (m): "))
    except ValueError:
        print("❌ Error: Asegúrese de ingresar números válidos para Edad, Peso y Estatura.")
        continue

    # 2. Control de edad mínima
    if edad < 14:
        print("🛑 Mensaje del Sistema: La persona no puede ingresar aún (edad mínima 14 años).")
        continuar = input("¿Desea registrar otro cliente? (si/no): ").lower()
        if continuar != 'si':
            break
        continue

    # 3. Cálculo de IMC, Diagnóstico, TMB y Rutina
    imc = calcular_imc(peso, estatura)
    diagnostico, recomendacion = obtener_diagnostico_y_recomendacion(imc)
    rutina_inicial = asignar_rutina_inicial(diagnostico)
    tmb = calcular_tmb(peso, estatura, edad, sexo)
    
    # --- Selección de Plan y Pago ---
    print("\n--- Planes de Afiliación ---")
    print("1. Básico ($60.000) | 2. Plata ($85.000) | 3. Oro ($100.000)")
    # (Código para seleccionar plan...)
    while True:
        plan_opcion = input("Seleccione el número del plan (1, 2, 3): ")
        if plan_opcion == '1':
            plan_seleccionado = "Basico"
            break
        elif plan_opcion == '2':
            plan_seleccionado = "Plata"
            break
        elif plan_opcion == '3':
            plan_seleccionado = "Oro"
            break
        else:
            print("Selección de plan inválida.")

    print("\n--- Modalidad de Pago ---")
    print("1. Transferencia | 2. Tarjeta")
    # (Código para seleccionar pago...)
    while True:
        pago_opcion = input("Seleccione el número de la modalidad de pago (1, 2): ")
        if pago_opcion == '1':
            modalidad_pago = "Transferencia"
            break
        elif pago_opcion == '2':
            modalidad_pago = "Tarjeta"
            break
        else:
            print("Selección de pago inválida.")


    # 4. Cálculo de costos
    valor_iva, costo_total_mensualidad, valor_base_plan = calcular_costo_y_iva(plan_seleccionado, modalidad_pago)
    
    # 5. Actualizar contadores administrativos
    clientes_registrados += 1
    ingresos_totales += costo_total_mensualidad
    ingresos_por_plan[plan_seleccionado] += costo_total_mensualidad
    ingresos_por_pago[modalidad_pago] += costo_total_mensualidad
    # Actualización del nuevo contador por Sede
    ingresos_por_sede[sede_seleccionada] += costo_total_mensualidad
    
    # 6. Generar Informe del Cliente
    print("\n" + "="*60)
    print("🧾 INFORME DE BIENVENIDA Y DIAGNÓSTICO (PERSONALIZADO)")
    print("="*60)
    print(f"**Sede de Afiliación:** {sede_seleccionada}")
    print(f"**Datos Personales:**")
    print(f"  - Nombres: {nombres} (Sexo: {sexo.capitalize()})")
    print(f"  - Edad: {edad} años | Documento: {documento} | Correo: {correo}")
    print("-" * 60)
    print(f"**Análisis de Salud Inicial:**")
    print(f"  - IMC: **{imc:.2f}** | Diagnóstico: **{diagnostico}**")
    print(f"  - Tasa Metabólica Basal (TMB): **{tmb:,.0f} calorías/día** (Energía en reposo)")
    print(f"  - Recomendación Nutricional Inicial: {recomendacion}")
    print("-" * 60)
    print(f"**Plan de Ejercicio Sugerido:**")
    print(f"  - **Rutina Inicial:** {rutina_inicial}")
    print("-" * 60)
    print(f"**Resumen de Costos:**")
    print(f"  - Plan Seleccionado: **{plan_seleccionado}** (Base: ${valor_base_plan:,.0f})")
    print(f"  - Modalidad de Pago: {modalidad_pago}")
    print(f"  - Valor del IVA ({int(IVA_PERCENTAGE*100)}%): ${valor_iva:,.0f}")
    print(f"  - **COSTO TOTAL MENSUALIDAD: ${costo_total_mensualidad:,.0f}**")
    print("="*60)

    # 7. Control del ciclo
    continuar = input("¿Desea registrar otro cliente? (si/no): ").lower()
    if continuar != 'si':
        break

# --- Fin del Programa y Resumen del Día ---
print("\n" + "#"*60)
print("🏁 PROGRAMA FINALIZADO - RESUMEN ADMINISTRATIVO DE LA JORNADA")
print("#"*60)
print(f"Número de personas registradas: **{clientes_registrados}**")
print(f"Total ingresos en $: **${ingresos_totales:,.0f}**")
print("-" * 60)

print("📈 Desglose de Ingresos por Sede:")
for sede, ingreso in ingresos_por_sede.items():
    print(f"  - Sede {sede}: ${ingreso:,.0f}")
    
print("-" * 60)
print("💰 Desglose de Ingresos por Plan:")
for plan, ingreso in ingresos_por_plan.items():
    print(f"  - {plan}: ${ingreso:,.0f}")

print("\n💳 Desglose de Ingresos por Modalidad de Pago:")
for pago, ingreso in ingresos_por_pago.items():
    print(f"  - {pago}: ${ingreso:,.0f}")

print("#"*60)