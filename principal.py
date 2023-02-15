import actualizar
import borrar
import insertar
import leer

class Programa:
    def init(self):
        self.dato=1

    def menu(self):
        opciones = {
            1: {"nombre": "Modificar Empresa", "funciones": {
                1: {"nombre": "Leer Empresa", "funcion": leer.consultarempresa},
                2: {"nombre": "Actualizar Empresa", "funcion": actualizar.updateempresa},
                3: {"nombre": "Borrar Empresa", "funcion": borrar.deleteempresa},
                4: {"nombre": "Insertar Empresa", "funcion": insertar.insertempresa}
            }},
            2: {"nombre": "Modificar Carrera", "funciones": {
                1: {"nombre": "Leer Carrera", "funcion": leer.consultarCarrera},
                2: {"nombre": "Actualizar Carrera", "funcion": actualizar.updatecarrera},
                3: {"nombre": "Borrar Carrera", "funcion": borrar.deleteCarrera},
                4: {"nombre": "Insertar Carrera", "funcion": insertar.insertcarrera}
            }},
            3: {"nombre": "Modifcar Estudiante", "funciones": {
                1: {"nombre": "Leer Estudiante", "funcion": leer.consultarestudiante},
                2: {"nombre": "Actualizar Estudiante", "funcion": actualizar.updateestudiante},
                3: {"nombre": "Borrar Estudiante", "funcion": borrar.deleteestudiante},
                4: {"nombre": "Insertar Estudiante", "funcion": insertar.insertestudiante}
            }},
            4: {"nombre": "Modifcar cordinador", "funciones": {
                1: {"nombre": "Leer cordinador", "funcion": leer.consultarcordinador},
                2: {"nombre": "Actualizar cordinador", "funcion": actualizar.updatecordinador},
                3: {"nombre": "Borrar cordinador", "funcion": borrar.deletecordinador},
                4: {"nombre": "Insertar cordinador", "funcion": insertar.insertcordinador}
            }},
            5: {"nombre": "Modifcar Horario", "funciones": {
                1: {"nombre": "Leer seguimiento", "funcion": leer.consultarseguimiento},
                2: {"nombre": "Actualizar seguimiento", "funcion": actualizar.updateseguimiento},
                3: {"nombre": "Borrar seguimiento", "funcion": borrar.deleteseguimiento},
                4: {"nombre": "Insertar seguimiento", "funcion": insertar.insertseguimiento}
            }},
        }
        
        
        for k, v in opciones.items():
            print(k, v["nombre"])
        try:
            opcion_seleccionada = int(input("Selecciona una opción: "))
            if opcion_seleccionada in opciones:
                funciones_seleccionadas = opciones[opcion_seleccionada]["funciones"]
                for k, v in funciones_seleccionadas.items():
                    print(k, v["nombre"])
                try:
                    funcion_seleccionada = int(input("Selecciona una función: "))
                    if funcion_seleccionada in funciones_seleccionadas:
                        funciones_seleccionadas[funcion_seleccionada]["funcion"]()
                    else:
                        print("La función seleccionada no existe.")
                except ValueError:
                    print("Debe ingresar un número entero.")
            else:
                print("La opción seleccionada no existe.")
        except ValueError:
            print("Debe ingresar un número entero.")

                
mongo =Programa()
mongo.menu()