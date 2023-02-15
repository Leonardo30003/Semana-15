from pymongo import MongoClient

cliente = MongoClient('localhost:27017')

db = cliente.PracticasPreprofesionales

def insertestudiante():
    counter = db.counter.find_one_and_update({"id": "estudianteId"}, {"$inc": {"seq": 1}}, upsert=True)
    if counter:
        estudianteId = counter["seq"]
    else:
        estudianteId = 1

    try:
        nombres = input('Ingresa los nombres -> ')  
        apellidos = input('Ingresa los apellidos -> ')
        cedula = input('Ingresa la cedula -> ')
        correo_institucional = input('Ingresa el correo Institucional -> ')
        direccion = input('Ingresa la direccion -> ')
        telefono = input('Ingresa el telefono -> ')
        while db.estudiante.find_one({"id": estudianteId}):
            estudianteId = estudianteId + 1
        db.estudiante.insert_one({
            "id": float( estudianteId),
            "nombres": nombres,
            "Apellidos": apellidos,
            "Cedula": cedula,
            "Correo_institucional": correo_institucional,
            "direccion": direccion,
            "telefono": telefono
        })
    except ImportError:
        print("Error de base de datos") 

def insertempresa():
    counter = db.counter.find_one_and_update({"id": "empresaId"}, {"$inc": {"seq": 1}}, upsert=True)
    if counter:
        empresaId = counter["seq"]
    else:
        empresaId = 1


    try:
        nombre= input("Ingrese el nombre de la empresa -> ")
        direccion = input("Ingrese la direccion -> ")
        telefono = input('Ingresa el telefono -> ')
        correo_electronico= input('Ingresa el correo electronico -> ')
        while db.empresa.find_one({"id": empresaId}):
            empresaId = empresaId + 1
        db.empresa.insert_one({
            "id": float(empresaId),
            "nombre" : nombre,
            "direccion": direccion,
            "telefono": telefono,
            "correo_electronico": correo_electronico
        })
    except ImportError:
        print("Error de base de datos")

def insertcarrera():
    counter = db.counter.find_one_and_update({"id": "carreraId"}, {"$inc": {"seq": 1}}, upsert=True)
    if counter:
        carreraId = counter["seq"]
    else:
        carreraId = 1
    try:
        nombre= input("Ingrese el nombre de la empresa -> ")
        descripcion = input("Ingrese la direccion -> ")
        while db.carrera.find_one({"id": carreraId}):
            carreraId = carreraId + 1
        db.carrera.insert_one({
            "id": float(carreraId),
            "Nombre" : nombre,
            "descripcion": descripcion
        })
    except ImportError:
        print("Error de base de datos")

def insertcordinador():
    counter = db.counter.find_one_and_update({"id": "visitaId"}, {"$inc": {"seq": 1}}, upsert=True)
    if counter:
        visitaId = counter["seq"]
    else:
        visitaId = 1
    
    try:
        nombre= input("Ingresa nobre del cordinador -> ")
        correoelectronico = input("Ingrese el correo electronico -> ")
        identificacion = input("Ingrese la identificacion -> ")
        departamento = input("Ingrese el departamento al que pertenece -> ")
        while db.visita.find_one({"id": visitaId}):
            visitaId = visitaId + 1

        db.visita.insert_one({
            "id": float(visitaId),
            "nobre" : nombre,
            "correoelectronico": correoelectronico,
            "identificacion": identificacion,
            "departamento": departamento
        })
    except ImportError:
        print("Error de base de datos")

def insertseguimiento():
    counter = db.counter.find_one_and_update({"id": "horarioId"}, {"$inc": {"seq": 1}}, upsert=True)
    if counter:
        horarioId = counter["seq"]
    else:
        horarioId = 1
    
    try:
        fechaInicio= input("Ingresa la fechaInicio -> ")
        fechaFin = input("Ingresa la fechaFin -> ")
        cantidadHoras= input("Ingrese la cantidadHoras -> ")
        tareas = input("Ingrese la carrera -> ")
        estado=input("Ingrese el estado -> ")
        id_estudiante=float(input("Ingrese el id del estudiante -> "))
        id_empresa=float(input("Ingrese la carrera -> "))
        id_cordinador=float(input("Ingrese la carrera -> "))
        
        while db.horario.find_one({"id": horarioId}):
            horarioId = horarioId + 1

        db.horario.insert_one({
            "id": float(horarioId),
            "fechaInicio" : fechaInicio,
            "fechaFin": fechaFin,
            "cantidadHoras": cantidadHoras,
            "tareas": tareas,
            "id_estudiante":id_estudiante
            "id_empresa":id_empresa
            "id_cordinador":id_cordinador

            
        })
    except ImportError:
        print("Error de base de datos")
