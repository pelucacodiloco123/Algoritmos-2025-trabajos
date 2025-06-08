from list_ import List

class Alumno:
    def __init__(self, nombre, apellido, legajo):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.parciales = List()

    def agregar_parcial(self, parcial):
        self.parciales.append(parcial)

    def mostrar_parciales(self):
        for parcial in self.parciales:
            print(parcial)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Legajo: {self.legajo}"


class Parcial:
    def __init__(self, materia, nota, fecha):
        self.materia = materia
        self.nota = nota
        self.fecha = fecha

    def __str__(self):
        return f"{self.materia} - Nota: {self.nota} - Fecha: {self.fecha}"


def order_by_name(value):
    return value.nombre

def order_by_apellido(value):
    return value.apellido

def order_by_legajo(value):
    return value.legajo

def order_by_materia(parcial):
    return parcial.materia
    
def order_by_nota(parcial):
    return parcial.nota
   
    
def order_by_fecha(parcial):
    return parcial.fecha
   
alumnos = List()

alumnos.append(Alumno("Juan", "Pérez", 12345))
alumnos.append(Alumno("Ana", "Gómez", 67890))
alumnos.append(Alumno("Carlos", "López", 54321))


alumnos[0].agregar_parcial(Parcial("Algoritmos y Estructuras de Datos", 8, "2023"))
alumnos[0].agregar_parcial(Parcial("Historia", 7, "2023"))

alumnos[1].agregar_parcial(Parcial("Base de Datos", 9, "2020"))
alumnos[1].agregar_parcial(Parcial("Matematicas", 5, "2023"))

alumnos[2].agregar_parcial(Parcial("Fisica", 3, "2023"))

alumnos.add_criterion("nombre", order_by_name)
alumnos.add_criterion("apellido", order_by_apellido)
alumnos.add_criterion("legajo", order_by_legajo)

def order_by_materiaa(alumno):
    for alumno in alumnos:
        alumno.parciales.add_criterion("materia", order_by_materia)

def order_by_notaa(alumno):
    for alumno in alumnos:
        alumno.parciales.add_criterion("nota", order_by_nota)

def order_by_fechaa(alumno):
    for alumno in alumnos:
        alumno.parciales.add_criterion("fecha", order_by_fecha)


alumnos.sort_by_criterion("apellido")


def alumnos_sin_desaprobados(lista_alumnos):
    resultado = List()
    for alumno in lista_alumnos:
        if alumno.parciales:
            tiene_desaprobado = False
            for parcial in alumno.parciales:
                if parcial.nota < 4:
                    tiene_desaprobado = True
                    break
            if not tiene_desaprobado:
                resultado.append(alumno)
    return resultado

def alumnos_promedio_89(lista_alumnos):
    resultado = List()
    for alumno in lista_alumnos:
        if alumno.parciales:
            tiene_desaprobado = False
            for parcial in alumno.parciales:
                if parcial.nota < 4:
                    tiene_desaprobado = True
                    break
            if not tiene_desaprobado and parcial.nota >= 8.9:
                resultado.append(alumno)
    return resultado


def alumnos_apellidoL(lista_alumnos):
    resultado = List()
    for alumno in lista_alumnos:
        if alumno.apellido[0] == "L":
            resultado.append(alumno)
    return resultado

def promediocadaalumno(lista_alumnos):
    for alumno in lista_alumnos:
        if alumno.parciales:
            promedio = sum(parcial.nota for parcial in alumno.parciales) / len(alumno.parciales)
            print(f"El promedio de {alumno.nombre} {alumno.apellido} es {promedio:}")


def algoritmos(lista_alumnos):
    encontrado = False
    resultado = List()
    
    for alumno in lista_alumnos:
        index = alumno.parciales.search("Algoritmos y Estructura de Datos", "materia")
        if index is not None:
            resultado.append(alumno)
            encontrado = True

    if not encontrado:
        print("No se encontraron parciales de Algoritmos en la lista de alumnos.")
    
    return resultado

def alumnoporcentajeaprobado(lista_alumnos):
  nombre = input("Ingrese el nombre del alumno: ")

  index = lista_alumnos.search(nombre, "nombre")
  if index is not None:
    alumno = lista_alumnos[index]
    if alumno.parciales:
        aprobados = sum(1 for parcial in alumno.parciales if parcial.nota >= 4)
        porcentaje_aprobados = (aprobados / len(alumno.parciales)) * 100
        print(f"El porcentaje de parciales aprobados de {alumno.nombre} {alumno.apellido} es {porcentaje_aprobados:.2f}")
    else:
        print("El alumno no tiene parciales registrados o no existe.")


def basededatos(lista_alumnos):
    encontrado = False
    aprobados = List()
    desaprobados = List()
    
    for alumno in lista_alumnos:
        index = alumno.parciales.search("Base de Datos", "materia")
        if index is not None and alumno.parciales[index].nota >= 4:
            aprobados.append(alumno)
            encontrado = True
        elif index is not None and alumno.parciales[index].nota < 4:
            desaprobados.append(alumno)
            encontrado = True

    if not encontrado:
        print("No se encontraron parciales de Base de Datos en la lista de alumnos.")
    
    return aprobados, desaprobados

def rendido2020(lista_alumnos):
    resultado = List()
    encontrado = False

    for alumno in lista_alumnos:
        alumno.parciales.add_criterion("fecha", order_by_fecha)
        index = alumno.parciales.search("2020", "fecha")
        if index is not None:
            resultado.append(alumno)
            encontrado = True

    if not encontrado:
        print("No se encontraron parciales de 2020.")
        
    return resultado

alumnos.show()
(alumnos_sin_desaprobados(alumnos)).show()
(alumnos_promedio_89(alumnos)).show()
(alumnos_apellidoL(alumnos)).show()
promediocadaalumno(alumnos)
(algoritmos(alumnos)).show()
print(alumnoporcentajeaprobado(alumnos))
print(basededatos(alumnos))
(rendido2020(alumnos)).show()