from pymongo import MongoClient

cliente = MongoClient('localhost:27017')
db = cliente.Pregunta8
def deleteempresa():
    try:
        criteria = input("\n Ingrese el id de la empresa a borrar -> ")
        db.empresa.delete_many(
            {"id": float(criteria)}
        )
        print(f"Registro {criteria} eliminado ")
    except ImportError:
        print("Deleting")

def deleteestudiante():
    try:
        criteria = input("\n Ingrese el id de la empresa a borrar -> ")
        db.estudiante.delete_many(
            {"id": float(criteria)}
        )
        print(f"Registro {criteria} eliminado ")
    except ImportError:
        print("Deleting")

def deletecordinador():
    try:
        criteria = input("\n Ingrese el id de la empresa a borrar -> ")
        db.horario.delete_many(
            {"id": float(criteria)}
        )
        print(f"Registro {criteria} eliminado ")
    except ImportError:
        print("Deleting")

def deleteseguimiento():
    try:
        criteria = input("\n Ingrese el id de la empresa a borrar -> ")
        db.visita.delete_many(
            {"id": float(criteria)}
        )
        print(f"Registro {criteria} eliminado ")
    except ImportError:
        print("Deleting")

def deleteCarrera():
    try:
        criteria = input("\n Ingrese el id de la empresa a borrar -> ")
        db.carrera.delete_many(
            {"id": float(criteria)}
        )
        print(f"Registro {criteria} eliminado ")
    except ImportError:
        print("Deleting")