def mochila_fuerza_bruta():
    print("========================================")
    print("   MOCHILA: ENFOQUE FUERZA BRUTA (LINEAL) ")
    print("========================================\n")
    
    n = int(input("Cantidad de objetos: "))
    
    pesos = [0] * n
    valores = [0] * n
    
    for i in range(n):
        pesos[i] = int(input(f"Peso del objeto {i + 1}: "))
        valores[i] = int(input(f"Valor del objeto {i + 1}: "))
        
    capacidad = int(input("Capacidad de la mochila: "))
    
    peso_total = 0
    valor_total = 0
    
    # --- NUEVA PARTE: SEGUIMIENTO PASO A PASO ---
    print("\n========================================")
    print("   SEGUIMIENTO DE DECISIONES EN VIVO    ")
    print("========================================")
    print(f"Capacidad Inicial de la Mochila: {capacidad}\n")
    
    for i in range(n):
        print(f"Evaluando Objeto {i + 1} -> Peso: {pesos[i]}, Valor: {valores[i]}")
        
        if peso_total + pesos[i] <= capacidad:
            peso_total += pesos[i]
            valor_total += valores[i]
            print(f"   [ACEPTADO] -> El objeto entra. Peso actual: {peso_total}/{capacidad}, Valor acumulado: {valor_total}")
        else:
            print(f"   [RECHAZADO] -> Excede la capacidad libre. Mochila se mantiene en peso: {peso_total}/{capacidad}")
        print("-" * 50)
    # --------------------------------------------
            
    print("\n===============================")
    print("        RESULTADO FINAL        ")
    print("===============================")
    print(f"Peso total utilizado: {peso_total}")
    print(f"Valor máximo obtenido: {valor_total}")

if __name__ == "__main__":
    mochila_fuerza_bruta()