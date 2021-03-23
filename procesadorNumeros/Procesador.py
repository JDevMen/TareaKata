class Procesador:
    def procesadorText(self, numeros):
        respuesta = []
        if numeros == "":
            respuesta = [0, -1, -1, -1]
            return respuesta
        else:
            numeros = numeros.replace(" ", "")
            lista = numeros.split(",")

            respuesta.append(len(lista))

            if len(lista) == 1:
                respuesta.append(int(lista[0]))
                respuesta.append(int(lista[0]))
                respuesta.append(int(lista[0]))
            else:
                i = 1
                minimo = int(lista[0])
                maximo = int(lista[0])
                while i < len(lista):
                    elementoNum = int(lista[i])
                    if elementoNum < minimo:
                        minimo = elementoNum
                    if elementoNum > maximo:
                        maximo = elementoNum
                    i += 1
                respuesta.append(minimo)
                respuesta.append(maximo)
                respuesta.append(0)
                
            return respuesta
