class Procesador:
    def procesadorText(self, numeros):
        respuesta = []
        if numeros == "":
            respuesta = [0, 0, 0, 0]
            return respuesta
        else:
            respuesta.append(1)
            respuesta.append(0)
            respuesta.append(0)
            respuesta.append(0)
            return respuesta
