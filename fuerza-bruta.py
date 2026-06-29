def mochila_fuerza_bruta():
    # Leer cantidad de objetos
    n = int(input("Cantidad de objetos: "))
    
    pesos = [0] * n
    valores = [0] * n
# Leer datos de cada objeto
    for i in range(n):
        pesos[i] = int(input(f"Peso del objeto {i + 1}: "))
        valores[i] = int(input(f"Valor del objeto {i + 1}: "))    