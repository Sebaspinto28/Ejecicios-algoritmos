from App import App

def main():
    menu = {
    "postres": [
        {"nombre": "Torta de chocolate", "precio": 5.00, "cantidad": 10},
        {"nombre": "Torta de frutas", "precio": 4.50, "cantidad": 12},
        {"nombre": "Torta de helado", "precio": 6.00, "cantidad": 8}
    ],
    "cafes": [
        {"nombre": "Espresso", "precio": 2.00, "cantidad": 15, "tamaño": "pequeño", "es_descafeinado": False},
        {"nombre": "Capuccino", "precio": 3.00, "cantidad": 12, "tamaño": "mediano", "es_descafeinado": False},
        {"nombre": "Moka", "precio": 4.00, "cantidad": 10, "tamaño": "grande", "es_descafeinado": False}
    ],
    "jugos": [
        {"nombre": "Jugo de naranja", "precio": 3.00, "cantidad": 20, "sabor": "naranja", "contiene_azucar": True},
        {"nombre": "Jugo de manzana", "precio": 2.50, "cantidad": 18, "sabor": "manzana", "contiene_azucar": False},
        {"nombre": "Jugo de plátano", "precio": 2.00, "cantidad": 15, "sabor": "plátano", "contiene_azucar": False}
    ]
}

    app = App()
    app.start(menu)
main()