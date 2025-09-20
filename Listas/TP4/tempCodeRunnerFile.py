
    if index2 is not None:
        resultado.append(str(value[index2]))
    else:
        resultado.append(None)
    return resultado

        
def letraBMS(value):
    resultados = []
    for item in value:
        if item.nombre[0] in "BMS":
            resultados.append(item.nombre)
    return resultados

        