
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
is_price=0
is_name=""
pacientes={}
enfermos=[]
while True:
    main=(input("Que decea realizar\n1.registro y cobro de pacientes\n2.ver paciente\n3.salir\n--->"))
    if main=="1":
        
        nombre=(input("Escriba su nombre\n-->"))
        apellido=(input("Escriba su apellido\n-->"))
        cedula=(input("Escriba su cedula sin comas ni puntos\n-->"))
        ide=int(input("Escriba el id de su patologia\n-->"))
        
        for system in pathologies:
            for enfermedad in pathologies[system]:
                for k in enfermedad:
                    if ide==enfermedad.get("id"):
                     is_price= enfermedad.get("price")
                     is_name= enfermedad.get("name")
                     pacientes={
                     "nombre":nombre,
                     "apellido":apellido,
                      "ide":ide,
                     "precio":is_price,
                     "fermo":is_name
                    }
                    else:
                        pass
        print(f"-{nombre} {apellido} \n-V{cedula}\n-{is_name}\n-{is_price}$")
        
        
    elif main=="2":
        
        patologia=(input("introdusca la patologia\n--->")).capitalize()
        for category,desease in pacientes.items():
            for d in desease:
                if patologia==pacientes:                
                    enfermos.append(category,desease)
                    print(enfermos)

    elif main=="3":
        print("Hasta pronto")
        break
    
    else:
        print("opcion no valida")
        
