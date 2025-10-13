from heap import HeapMax

queque_empleados = HeapMax()

queque_empleados.arrive("EmpleadoA.doc", 1)
queque_empleados.arrive("EmpleadoB.doc", 1)
queque_empleados.arrive("EmpleadoC.doc", 1)

print(queque_empleados.elements[0][1]) #posicion 0, elemento 1 (el value)

queque_empleados.arrive("StaffTIA.doc", 2)
queque_empleados.arrive("StaffTIB.doc", 2)
queque_empleados.arrive("GerenteA.doc", 3)

for i in range (2): #el range funciona como n - 1, asi que el range(2) es desde 0 a 1
    print(queque_empleados.elements[i][1])


queque_empleados.arrive("EmpleadoD.doc", 1)
queque_empleados.arrive("EmpleadoE.doc", 1)
queque_empleados.arrive("GerenteB.doc", 3)

num = queque_empleados.size()

for i in range(num):
    print(queque_empleados.elements[i][1])
