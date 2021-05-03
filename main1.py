from time import sleep
from uuid import uuid4
from json import load, decoder, dump

datadocente = {"datos_docentes":[]}
dataalumno = {"datos_alumnos" :[]}
class docen:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def datos_docente(self):
        nombre = input("Ingrese el nombre del docente\n")
        edad = input("Ingrese la edad del docente\n")
        dni = input("Ingrese el dni del docente\n")
        print(f"\n Se ingresaron los datos del docente {nombre} con exito")
        nuevo_docente = docen(nombre, edad, dni)
        x = {
            "id": str(uuid4()),
            "nombre": nuevo_docente.nombre,
            "edad": nuevo_docente.edad,
            "dni": nuevo_docente.dni
        }
        datadocente["datos_docentes"].append(x)
        datadocente2 = datadocente["datos_docentes"]
        archivo = open("docentes.json","w")
        dump(datadocente2, archivo, indent=4 )
        archivo.close()

class alum:
    def __init__(self, nombre, listanotas, notamin, notamax, prom):
        self.nombre = nombre
        self.listanotas = listanotas
        self.notamin = notamin
        self.notamax = notamax
        self.prom = prom 

    def datos_alumno(self):
        listanotas =[]
        nombre = input("Ingrese el nombre del alumno\n")
        cantidadnotas = int(input("¿ Cuántas notas va a ingresar?\n"))-1
        while True:
            if len(listanotas) <= cantidadnotas:
                nota = int(input("Ingresar nota: "))
                listanotas.append(nota)
            else:
                print(f"\n Se ingresaron los datos del alumno {nombre} con exito")
                break
        notamin = str(min(listanotas))
        notamax = str(max(listanotas))
        prom = str(sum(listanotas)/len(listanotas))  
        print(f"Las notas ingresadas son: {listanotas}\n")
        print(f'Nota maxima: {max(listanotas)}\n')
        print(f'Nota minima: {min(listanotas)}\n')
        print(f'Nota promedio: {sum(listanotas)/len(listanotas)}\n')
        nuevo_alum = alum(nombre, listanotas, notamin, notamax, prom)
        y = {
            "nombre": nuevo_alum.nombre,
            "notas": nuevo_alum.listanotas,
            "nota promedio": nuevo_alum.prom,
            "nota maxima": nuevo_alum.notamax,
            "nota minima" : nuevo_alum.notamin
        }
        dataalumno["datos_alumnos"].append(y)
        dataalumno2 = dataalumno["datos_alumnos"]
        archivo = open("alumnos.json", "w")
        dump(dataalumno2, archivo, indent=4 )
        archivo.close()   

class start(docen, alum):
    def __init__(self):
        try:
            archivo1 = open("docentes.json", "r")
            datadocente["datos_docentes"] = load(archivo1)
            archivo1.close()
            archivo2 = open("alumnos.json", "r")
            dataalumno["datos_alumnos"] = load(archivo2)
            archivo2.close()
        except FileNotFoundError:
            print("\n Creando base de registro de docentes...")
            sleep(1)
            archivo1 = open("docentes.json", "w")
            archivo1.close()
            print("\n Creando base de registro de alumnos...")
            sleep(1)
            archivo2 = open("alumnos.json", "w")
            archivo2.close()
        except decoder.JSONDecodeError:
            print("\nNo hay archivos creados, se puede crear desde ahora")
        except KeyboardInterrupt:
            print("\nIntente nuevamente")
        try:
            while True:
                print("""
                 Bienvenido al portal educativo:
                    ¿Que desea hacer?
                    1) Ingresar datos del docente
                    2) Ingresar datos del alumno
                    3) salir\n
                 """)
                opcion = input("> ")
                if opcion == "1":
                    self.datos_docente()
                elif opcion == "2":
                    self.datos_alumno()
                elif opcion =="3":
                    print("\nGracias por usar el portal educativo")
                    sleep(1)
                    quit()
                else:
                    print("\n Introduciste una opcion incorrecta")
        except KeyboardInterrupt:
            print("\nIntente nuevamente")
start()