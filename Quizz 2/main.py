from App import App
def main():
    datos  = {
  "eventos": [
    {
      "id": 1,
      "tipo": "Concierto",
      "fecha": "2023-05-15",
      "hora": "20:00",
      "duracion": 120,
      "lugar": "Teatro Principal",
      "artistas": []
    },
    {
      "id": 2,
      "tipo": "Comedy Show",
      "fecha": "2023-05-20",
      "hora": "19:00",
      "duracion": 90,
      "lugar": "Club de Comedia",
      "artistas": []
    },
    {
      "id": 3,
      "tipo": "Festival de Música",
      "fecha": "2023-06-10",
      "hora": "16:00",
      "duracion": 240,
      "lugar": "Parque Central",
      "artistas": []
    }
  ],
  "artistas": [
    {
      "nombre": "Juan Pérez",
      "biografia": "Músico de gran trayectoria",
      "tipo": "Músico",
      "tarifa_hora": 100.0,
      "instrumento": "Guitarra",
      "eventos": []
    },
    {
      "nombre": "María Gómez",
      "biografia": "Comediante reconocida",
      "tipo": "Comediante",
      "tarifa_hora": 80.0,
      "especialidad": "Stand-up",
      "eventos": []
    },
    {
      "nombre": "Pedro Martínez",
      "biografia": "DJ de música electrónica",
      "tipo": "DJ",
      "tarifa_hora": 120.0,
      "genero_musical": "Techno",
      "eventos": []
    },
    {
      "nombre": "Luis Sánchez",
      "biografia": "Comediante novato",
      "tipo": "Comediante",
      "tarifa_hora": 60.0,
      "especialidad": "Sketches",
      "eventos": []
    },
    {
      "nombre": "Ana Rodríguez",
      "biografia": "Talentosa violinista",
      "tipo": "Músico",
      "tarifa_hora": 110.0,
      "instrumento": "Violín",
      "eventos": []
    }
  ]
}
    app=App()
    app.start(datos)
main()