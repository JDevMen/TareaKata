class Procesador:
    def procesadorText(self, numeros):
        respuesta = []
        if numeros == "":
            respuesta = [0, 0, 0, 0]
            return respuesta
        else:
            lista = numeros.split(",")
            if len(lista) == 1:
                respuesta.append(1)
            else:
                respuesta.append(2)
            respuesta.append(0)
            respuesta.append(0)
            respuesta.append(0)
            return respuesta
