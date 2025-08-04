def OrdenarCarnet(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = int
        for clave, valor in lista.items():
            pivote = clave
            break
        mayores = {x for x in lista["carnet"] if x > pivote}
        menores = {x for x in lista["carnet"] if x < pivote}
        return OrdenarCarnet(menores) + [pivote] + OrdenarCarnet(mayores)
def OrdenarNombre(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista["carnet"]["nombre"]
        mayores = {x for x in lista["carnet"]["nombre"] if x > pivote}
        iguales = {x for x in lista["carnet"]["nombre"] if x == pivote}
        menores = {x for x in lista["carnet"]["nombre"] if x < pivote}
        return OrdenarNombre(menores) + iguales + OrdenarNombre(mayores)

estudiantes ={}
#cursos = {}
def mostrarDatos(estudiante):
    notaFinal = 0
    notaTotal = 0
    numCursos = 0
    for carnet, datos in estudiante.items():
        print(f"\nCarnet: {carnet}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Edad: {datos['edad']}")
        print(f"Carrera: {datos['carrera']}")
        print("\tCursos: ")
        for curso, nota in datos['nombreCurso'].items():
            print(f"Curso: {curso}")
            print(f"Nota de la tarea: {nota['notaTarea']}")
            print(f"Nota del Parcial: {nota['notaParcial']}")
            print(f"Nota del proyecto:{nota['notaProyecto']} ")
            numCursos += 1
            notaFinal = (nota['notaParcial'] + nota['notaProyecto']+ nota['notaTarea'])
            notaTotal += notaFinal
        print("\n Promedio final de todos los cursos: ")
        notaFinal = notaFinal/numCursos
        print(f"Nota final: {notaFinal}")




while True:
    print("1. Registrar estudiantes")
    print("2. Mostrar todos los estudiantes y sus cursos")
    print("3. Buscar estudiante por carnet")
    print("4. SALIR")
    opcion = int(input("Selecciona una opcion: "))
    match opcion:
        case 1:
            cantidad = int(input("Cuantos estudiantes desea ingresar?: "))
            for i in range(cantidad):
                carnet = input("Ingresa carnet del estudiante: ")
                nombre = input("Ingresa nombre completo del estudiante: ")
                edad = int(input("Ingresa edad del estudiante: "))
                carrera = input("Ingresa carrera del estudiante: ")
                estudiantes[carnet] = {
                    "nombre": nombre,
                    "edad": edad,
                    "carrera": carrera,
                }
                cantidadCursos = int(input("Cuantos cursos desea ingresar?: "))
                if cantidadCursos > 0:
                    for x in range(cantidadCursos):
                        nombreCurso = input("Ingresa nombre del curso: ")
                        notaTarea = int(input("Ingresa nota de la tarea del curso: "))
                        if notaTarea<=60 and notaTarea>=0:
                            notaParcial = int(input("Ingresa nota del parcial del curso: "))
                            if notaParcial<=20 and notaParcial>=0:
                                notaProyecto = int(input("Ingresa nota del proyecto del curso: "))
                                if notaProyecto<=20 and notaProyecto>=0:
                                    estudiantes[nombreCurso] = {
                                    "notaTarea": notaTarea,
                                    "notaParcial": notaParcial,
                                    "notaProyecto": notaProyecto,
                                    }
                                else:
                                    print("Ingrese una nota correcta.")
                            else:
                                print("Ingrese una nota correcta.")
                        else:
                            print("Ingrese una nota correcta.")


                else:
                    print("Ingrese una cantidad correcta.")

        case 2:
            print("Todos los estudiantes registrados.")
            print("Estudiantes ordenados por su Carnet")
            estudiantesOrdenadosCarnet = OrdenarCarnet(estudiantes)
            print(mostrarDatos(estudiantesOrdenadosCarnet))
            print("Estudiantes ordenados por su Nombre: ")
            estudiantesOrdenadosNombre = OrdenarNombre(estudiantes)
            print(mostrarDatos(estudiantesOrdenadosNombre))
        case 3:
            buscar = input("Ingrese el carnet del estudiante: ")
            if buscar in estudiantes:
                estudiante = estudiantes[buscar]
                print(f"Nombre: {estudiante['nombre']}")
                print(f"Edad: {estudiante['edad']}")
                print(f"Carrera: {estudiante['carrera']}")
                print("\tCursos: ")
                for curso, nota in estudiante['cursos'].items():
                    print(f"Curso: {curso}")
                    print(f"Nota de la tarea: {nota['notaTarea']}")
                    print(f"Nota del Parcial: {nota['notaParcial']}")
                    print(f"Nota del proyecto: {nota['notaProyecto']}")
            else:
                print("Estudiante no encontrado.")
        case 4:
            print("Saliendo...")
            break