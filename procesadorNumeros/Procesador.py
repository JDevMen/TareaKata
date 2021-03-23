class Procesador:
    def procesadorText(self, numeros):
        respuesta = []
        if numeros == "":
            respuesta = [0, -1, 0, 0]
            return respuesta
        else:
            numeros = numeros.replace(" ", "")
            lista = numeros.split(",")

            respuesta.append(len(lista))

            if len(lista) == 1:
                respuesta.append(int(lista[0]))
            else:
                elementoA = int(lista[0])
                elementoB = int(lista[1])

                if elementoA < elementoB:
                    respuesta.append(elementoA)
                else:
                    respuesta.append(elementoB)
            respuesta.append(0)
            respuesta.append(0)
            return respuesta
