from pymongo import MongoClient

cliente = MongoClient('localhost:27017')
db = cliente.Pregunta8


def updateestudiante():
    criteria = input("\n Ingrese el id del registro a actulizar -> ")

    nombre = input('Ingresa los nombres  -> ')
    apellidos = float(input('Ingresa los apellidos -> '))
    cedula = input('Ingresa la cedula -> ')
    correo_instutucional = input('Ingresa el correo Institucional -> ')
    direccion = input('Ingresa la direccion -> ')
    telefono = input('Ingresa el telefono -> ')
    id_carrera= float(input('Ingresa el id_carrera -> '))
    id_empresa =float(input('Ingresa el id empresa -> '))

    db.estudiante.update_one(
        {"id": float(criteria)},
        {

            "$set": {
                "nombres": nombre,
                "apellidos": apellidos,
                "cedula": cedula,
                "correo_instutucional": correo_instutucional,
                "direccion": direccion,
                "telefono": telefono,
                "id_carrera" : id_carrera,
                "id_Empresa" : id_empresa

            }
        }
    )
    print("================================================================")
    print("*********************Registro actualizado***********************")
    print("================================================================")


def updateempresa():
    criteria = input("\n Ingrese el id del registro a actulizar -> ")

    nombre = input("Ingrese el nombre de la empresa -> ")
    direccion = input("Ingrese la direccion -> ")
    telefono = input('Ingresa el telefono -> ')
    correo_electronico = input('Ingresa el correo electronico -> ')
    personaDeContacto = input('Ingresa el nombre de la persona d contacto')

    db.empresa.update_one(
        {"id": float(criteria)},
        {

            "$set": {
                "nombre": nombre,
                "direccion": direccion,
                "telefono": telefono,
                "correo_electronico": correo_electronico
                "personaDeContacto":personaDeContacto
            }
        }
    )
    print("================================================================")
    print("*********************Registro actualizado***********************")
    print("================================================================")


def updatecarrera():
    criteria = input("\n Ingrese el id del registro a actulizar -> ")

    nombre = input("Ingrese la carrera -> ")
    descripcion = input("Ingrese la descripcion -> ")

    db.carrera.update_one(
        {"id": float(criteria)},
        {

            "$set": {
                "nombre": nombre,
                "descripcion": descripcion
            }
        }
    )
    print("================================================================")
    print("*********************Registro actualizado***********************")
    print("================================================================")


def updatecordinador():
    criteria = input("\n Ingrese el id del registro a actulizar -> ")

    nombre = input("Ingresa nombre -> ")
    correoElectronico = input("Ingrese correoElectronico -> ")
    identificacion = input("Ingrese identificacion -> ")
    departamento = input("Ingrese el departamento al que pertenece -> ")

    db.horario.update_one(
        {"id": float(criteria)},
        {

            "$set": {
                "nombre": nombre,
                "correoElectronico": correoElectronico,
                "identificacion": identificacion,
                "departamento": departamento
            }
        }
    )
    print("================================================================")
    print("*********************Registro actualizado***********************")
    print("================================================================")


def updateseguimiento():
    criteria = input("\n Ingrese el id del registro a actulizar -> ")

    fechaInicio = input("Ingresa la fecha de Inicio -> ")
    fechaFin = input("Ingrese la fecha de Fin -> ")
    cantidadHoras = input("Ingrese la cantidad de horas -> ")
    tareas = input("Ingrese la tarea -> ")
    estado=input("estado")
    id_estudiante=float(input("ingrese el id del estudiante"))
    id_compañia=float(input("Ingrese el id de la compañia"))
    id_cordinador=float(input("Ingrese el id del cordinador"))


    db.visita.update_one(
        {"id": float(criteria)},
        {

            "$set": {
                "fechaInicio": fechaInicio,
                "fechaFin": fechaFin,
                "cantidadHoras": cantidadHoras,
                "tareas": tareas,
                "id_estudiante":id_estudiante,
                "id_compañia":id_compañia,
                "id_cordinador":id_cordinador
            }
        }
    )
    print("================================================================")
    print("*********************Registro actualizado***********************")
    print("================================================================")
