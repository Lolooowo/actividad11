def quickSort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    mayores = [x for x in lista[1:] if x > pivote]
    iguales = [x for x in lista if x == pivote]
    menores = [x for x in lista[1:] if x < pivote]
    return quickSort(menores) + iguales + quickSort(mayores)
estudiantes = []
num = int(input("Ingrese el numero de estudiantes que va a ingresar: "))
for x in range(num):
    nombre = input(f"Ingrese el nombre del estudiante No. {x + 1}: ")
    estudiantes.append(nombre)
ordenados = quickSort(estudiantes)
i = 0
for estudiante in ordenados:
    print("Los estudiantes son: ")
    print(f"No.{i+1} {estudiante}")
    i+= 1