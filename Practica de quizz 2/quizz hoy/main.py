from App import App

def main():
    datos = {
    "vehiculos": [
        {"id": 1, "tipo": "Automovil", "año": 2015, "color": "Azul", "precio": 200.0},
        {"id": 2, "tipo": "Camioneta", "año": 2018, "color": "Blanco", "precio": 250.0},
        {"id": 3, "tipo": "Motocicleta", "año": 2020, "color": "Rojo", "precio": 150.0},
        {"id": 4, "tipo": "Bicicleta", "año": 2022, "color": "Verde", "precio": 4.0},
        {"id": 5, "tipo": "Moto", "año": 2019, "color": "Negro", "precio": 8.0},
        {"id": 6, "tipo": "Automovil", "año": 2021, "color": "Gris", "precio": 220.0},
        {"id": 7, "tipo": "Camioneta", "año": 2020, "color": "Plata", "precio": 280.0},
        {"id": 8, "tipo": "Motocicleta", "año": 2022, "color": "Amarillo", "precio": 170.0}
    ],
    "clientes": [
        {"nombre": "Juan Pérez", "ci": "12345678", "tipo": "personal"},
        {"nombre": "Empresa S.A.", "ci": "18654321", "tipo": "juridico"},
        {"nombre": "Carlos Fernández", "ci": "35765432", "tipo": "personal"},
        {"nombre": "María Gómez", "ci": "28765432", "tipo": "personal"},
        {"nombre": "Industrias Unidas S.A.", "ci": "17654321", "tipo": "juridico"},
        {"nombre": "Ana Rodríguez", "ci": "14321987", "tipo": "personal"}
    ]
}
    app = App()
    app.start(datos)
main()