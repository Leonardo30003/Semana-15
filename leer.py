from pymongo import MongoClient

cliente = MongoClient('localhost:27017')
db = cliente.Pregunta8

def consultarestudiante():
    try:
        estudiantes = db.estudiante.find()
        print("Presentacion")

        for i in estudiantes:
            print(i)
    except ImportError:
        print("Error")

def consultarseguimiento():
    try:
        visitas = db.visita.find()
        print("Presentacion")

        for i in visitas:
            print(i)
    except ImportError:
        print("Error")

def consultarcordinador():
    try:
        horarios = db.horario.find()
        print("Presentacion")

        for i in horarios:
            print(i)
    except ImportError:
        print("Error")

def consultarempresa():
    try:
        empresa = db.empresa.find()
        print("Presentacion")
        for i in empresa:
            print(i)
    except ImportError:
        print("Error")

def consultarCarrera():
    try:
        carrera = db.carrera.find()
        print("Presentacion")

        for i in carrera:
            print(i)
    except ImportError:
        print("Error")