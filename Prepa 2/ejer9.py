#     Se ha solicitado un programa que facilite la gestión del inventario de una floristería 💐 a final de mes.
#Se otorgarán 2 listas, flores que almacena los nombres de todas las flores, e inventario_flores que almacena “Cantidad Disponible”, “Precio por Unidad”, “Último Restock”, y “Vendidas” respectivamente. Su tarea es mostrar al usuario el inventario de manera amigable, permitiéndole ingresar el nombre de una flor para visualizar su información.
#Bono (1.5pts): Deberá guardar la información de ambas listas en una estructura de datos que facilite su almacenamiento (diccionario)
#Ejemplo: 
#inventario = {
#“Rosa”: {“Cantidad Disponible”: 20, “Precio por Unidad”: 1.50, “Último Restock”: "2024-
#05-01", “Vendidas”: 50},
#.
#.
#}
#Estructuras para utilizar:

flores = ["Rosa", "Tulipán", "Orquídea", "Lirio", "Girasol", "Clavel", "Margarita", "Jazmín", "Dalia", "Peonía"]
dic={}
inventario_flores = [
    [20, 1.50, "2024-05-01", 50],  
    [15, 2.00, "2024-04-28", 30],  
    [10, 3.00, "2024-04-30", 25],  
    [25, 1.20, "2024-05-02", 40],
    [18, 2.50, "2024-04-27", 35],  
    [30, 0.80, "2024-05-01", 45],  
    [22, 1.00, "2024-04-29", 20],  
    [12, 2.20, "2024-04-28", 15],  
    [8, 1.70, "2024-05-03", 10],   
    [14, 2.80, "2024-05-01", 25]
]

for flor in range(len(flores)):
    dic[flores[flor]]={
        "cantidad":inventario_flores[flor][0],
        "precio":inventario_flores[flor][1],
        "fecha":inventario_flores[flor][2],
        "vendidas":inventario_flores[flor][3],
    }


busca=str(input("Que flor quieres buscar\n-->")).capitalize()
for x in dic:
        
        if busca==x:
            print(f"flor: {busca}\ncantidad:{dic[busca]["cantidad"]}\nprecio: {dic[busca]["precio"]}\nfecha:{dic[busca]["fecha"]}\nvendidas:{dic[busca]["vendidas"]} ")





