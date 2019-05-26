from pulp import pulp

# Ejemplo del problema de transporte  utilizando PuLP
# Variable prob que contiene los datos del problema
prob = pulp.LpProblem("Problema de distribución", pulp.LpMinimize)

# Creamos lista de Centros de Distribución o nodos de oferta
Centros_Distribucion = ["CEDI A", "CEDI B"]

# diccionario con la capacidad de oferta de cada CEDI
oferta = {"CEDI A": 10,
          "CEDI B": 20}

# Creamos la lista de los bares o nodos de demanda
plantas = ["Planta 1", "Planta 2", "Planta 3", "Planta 4", "Planta 5"]

# diccionario con la capacidad de demanda de cada Planta
demanda = {"Planta 1": 3,
           "Planta 2": 5,
           "Planta 3": 6,
           "Planta 4": 2,
           "Planta 5": 7, }

# Lista con los costos de transporte de cada nodo
costos = [  # Plantas
    # 1 2 3 4 5
    [26250, 73500, 106750, 105000, 32900],  # A   CEDIS
    [28700, 18200, 40250, 129500, 37450]  # B
]

# Converte los costos en un diccionario de PuLP
costos = pulp.makeDict([Centros_Distribucion, plantas], costos, 0)

# Tupla que contiene todas las posibles rutas de tranporte.
rutas = [(c, b) for c in Centros_Distribucion for b in plantas]

# El diccionario x contiene la candidad enviada en las rutas
x = pulp.LpVariable.dicts("ruta", (Centros_Distribucion, plantas),
                          lowBound=0,
                          cat=pulp.LpInteger)

# Función objetivo del problema
prob += sum([x[c][b] * costos[c][b] for (c, b) in rutas]), \
        "Suma_de_costos_de_transporte"

# Restricción de máxima oferta de cada Centro de distribución.
for c in Centros_Distribucion:
    prob += sum([x[c][b] for b in plantas]) <= oferta[c], \
            "Suma_de_Productos_que_salen_de_cervecerias_%s" % c

# Restricción de demanda mínima de cada planta
for b in plantas:
    prob += sum([x[c][b] for c in Centros_Distribucion]) >= demanda[b], \
            "Sum_of_Products_into_Planta%s" % b

# Los datos del problema son exportado a archivo .lp
prob.writeLP("problemaDeTransporte.lp")

# Resolviendo el problema.
prob.solve()

# Imprimimos el estado del problema.
print("Status: {}".format(pulp.LpStatus[prob.status]))

# Imprimimos cada variable con su solución óptima.
for v in prob.variables():
    print("{0:} = {1:}".format(v.name, v.varValue))

# Imprimimos el valor óptimo de la función objetivo
print("Costo total de transporte = {}".format(prob.objective.value()))

