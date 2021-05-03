nombre = input("Ingrese el nombre del alumno\n")
apellido = input("Ingrese el apellido\n")
print(f"Datos del alumno ingresado: {nombre} {apellido}")
notas = []
cantidadnotas = int(input("¿ Cuántas notas va a ingresar?\n"))-1
while (True):
    if len(notas) <= cantidadnotas:
        nota = int(input("Ingresar nota: "))
        notas.append(nota)
    else:
        break
print(f"Las notas ingresadas son: {notas}\n")
print(f'Nota máxima: {max(notas)}\n')
print(f'Nota mínima: {min(notas)}\n')
print(f'Nota promedio: {sum(notas)/len(notas)}\n')
archivo = dict(Nombre = nombre, Apellido = apellido, Notas = notas, Promedio = {sum(notas)/len(notas)}, Nota_máxima = {max(notas)}, Nota_mínima = {min(notas)})
print(f"Archivo: {archivo}")
print(len(notas))