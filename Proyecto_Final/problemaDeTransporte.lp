\* Problema de distribución *\
Minimize
Suma_de_costos_de_transporte: 26250 ruta_CEDI_A_Planta_1
 + 73500 ruta_CEDI_A_Planta_2 + 106750 ruta_CEDI_A_Planta_3
 + 105000 ruta_CEDI_A_Planta_4 + 32900 ruta_CEDI_A_Planta_5
 + 28700 ruta_CEDI_B_Planta_1 + 18200 ruta_CEDI_B_Planta_2
 + 40250 ruta_CEDI_B_Planta_3 + 129500 ruta_CEDI_B_Planta_4
 + 37450 ruta_CEDI_B_Planta_5
Subject To
Sum_of_Products_into_PlantaPlanta_1: ruta_CEDI_A_Planta_1
 + ruta_CEDI_B_Planta_1 >= 3
Sum_of_Products_into_PlantaPlanta_2: ruta_CEDI_A_Planta_2
 + ruta_CEDI_B_Planta_2 >= 5
Sum_of_Products_into_PlantaPlanta_3: ruta_CEDI_A_Planta_3
 + ruta_CEDI_B_Planta_3 >= 6
Sum_of_Products_into_PlantaPlanta_4: ruta_CEDI_A_Planta_4
 + ruta_CEDI_B_Planta_4 >= 2
Sum_of_Products_into_PlantaPlanta_5: ruta_CEDI_A_Planta_5
 + ruta_CEDI_B_Planta_5 >= 7
Suma_de_Productos_que_salen_de_cervecerias_CEDI_A: ruta_CEDI_A_Planta_1
 + ruta_CEDI_A_Planta_2 + ruta_CEDI_A_Planta_3 + ruta_CEDI_A_Planta_4
 + ruta_CEDI_A_Planta_5 <= 10
Suma_de_Productos_que_salen_de_cervecerias_CEDI_B: ruta_CEDI_B_Planta_1
 + ruta_CEDI_B_Planta_2 + ruta_CEDI_B_Planta_3 + ruta_CEDI_B_Planta_4
 + ruta_CEDI_B_Planta_5 <= 20
Bounds
0 <= ruta_CEDI_A_Planta_1
0 <= ruta_CEDI_A_Planta_2
0 <= ruta_CEDI_A_Planta_3
0 <= ruta_CEDI_A_Planta_4
0 <= ruta_CEDI_A_Planta_5
0 <= ruta_CEDI_B_Planta_1
0 <= ruta_CEDI_B_Planta_2
0 <= ruta_CEDI_B_Planta_3
0 <= ruta_CEDI_B_Planta_4
0 <= ruta_CEDI_B_Planta_5
Generals
ruta_CEDI_A_Planta_1
ruta_CEDI_A_Planta_2
ruta_CEDI_A_Planta_3
ruta_CEDI_A_Planta_4
ruta_CEDI_A_Planta_5
ruta_CEDI_B_Planta_1
ruta_CEDI_B_Planta_2
ruta_CEDI_B_Planta_3
ruta_CEDI_B_Planta_4
ruta_CEDI_B_Planta_5
End
