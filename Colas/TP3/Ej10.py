import queue_
import stack

class Aplicacion:
 def __init__(self,nombre,hora,mensaje):
    self.nombre=nombre
    self.hora=hora
    self.mensaje=mensaje
 def __str__(self):
        return f"{self.nombre} - {self.hora} - {self.mensaje}"
 

Smartphone=queue_.Queue()

Smartphone.arrive(Aplicacion("WhatsApp","12:00","Hola"))
Smartphone.arrive(Aplicacion("Instagram","12:01","Hola"))
Smartphone.arrive(Aplicacion("Facebook","12:02","Hola"))
Smartphone.arrive(Aplicacion("Facebook","10:02","Hola"))
Smartphone.arrive(Aplicacion("Facebook","22:02","Hola"))
Smartphone.arrive(Aplicacion("Twitter","11:43","Hola"))
Smartphone.arrive(Aplicacion("Twitter","12:03","Python"))
Smartphone.arrive(Aplicacion("Twitter","15:57","Python"))


def eliminar_facebook(Cola: queue_.Queue):
    for i in range(Cola.size()):
        if Cola.on_front().nombre != "Facebook":
            Cola.move_to_end()
        else:
            Cola.attention()
    return print("Se eliminaron todas las notificaciones de Facebook")

def mostrar_Twitter_Python(Cola: queue_.Queue):
    for i in range(Cola.size()):
        if Cola.on_front().nombre == "Twitter" and Cola.on_front().mensaje == "Python":
            print(Cola.on_front())
        Cola.move_to_end()
    return print("Se mostraron todas las notificaciones de Twitter con el mensaje Python")

def almacenar_por_hora(cola: queue_.Queue):
    Entremedioytarde = stack.Stack()
    se_agrego = False

    for i in range(cola.size()):
        if "11:43" <= cola.on_front().hora <= "15:57":
            Entremedioytarde.push(cola.on_front())
            se_agrego = True
        cola.move_to_end()

    if se_agrego:
        print("Se agregaron todas las notificaciones de entre la 11:43 y la 15:57 a la pila")
    else:
        print("No hay notificaciones dentro del rango horario especificado")


eliminar_facebook(Smartphone)
mostrar_Twitter_Python(Smartphone)
almacenar_por_hora(Smartphone)