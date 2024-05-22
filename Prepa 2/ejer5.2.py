
pathologies = {
    "Respiratory system": [
        {
            "id": 1,
            "name": "Cystic Fibrosis",
            "price": 300 	
        },
        {
            "id": 2,
            "name": "Emphysema",
            "price": 500
        },
        {
            "id": 3,
            "name": "Tuberculosis",
            "price": 450
        }
    ],
    "Nervous system": [
        {
            "id": 4,
            "name": "Parkinson",
            "price": 800 	
        },
        {
            "id": 5,
            "name": "Epilepsy",
            "price": 600
        }
    ],
    "Endocrine system": [
        {
            "id": 6,
            "name": "Diabetes",
            "price": 350 	
        },
        {
            "id": 7,
            "name": "Acromegaly",
            "price": 700
        },
        {
            "id": 8,
            "name": "Hashimoto’s thyroiditis",
            "price": 900
        }
    ],   
}

pacientes=[]
facturas=[]


while True:
    main=(input("Que decea realizar\n1.registro y cobro de pacientes\n2.ver paciente\n3.salir\n--->"))
    if main=="1":
        
        nombre=(input("Escriba su nombre\n-->"))
        apellido=(input("Escriba su apellido\n-->"))
        cedula=(input("Escriba su cedula sin comas ni puntos\n-->"))
        ide=int(input("Escriba el id de su patologia\n-->"))














    elif main=="2":
        pass
    elif main=="3":
        print("Hasta pronto")
        break
