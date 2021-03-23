from unittest import TestCase

from Procesador import Procesador
import random


class ProcesadorTest(TestCase):

    # def test_procesador_String_numero_elementos_Vacio(self):
    #     self.assertEqual(Procesador().procesadorText(""), [0, 0, 0, 0], "Arreglo vacío")
    #
    # def test_procesador_String_numero_elementos_un_Numero(self):
    #     self.assertEqual(Procesador().procesadorText("1"), [1, 0, 0, 0], "Arreglo con un número")
    #
    # def test_procesador_String_numero_elementos_dos_Numeros(self):
    #     self.assertEqual(Procesador().procesadorText("1,2"), [2, 0, 0, 0], "Arreglo con dos número")
    #
    # def test_procesador_String_numero_elementos_n_Numeros(self):
    #     numElementos = random.randint(3, 10)
    #     stringAProcesar = ""
    #
    #     if numElementos >= 1:
    #         i = 1
    #         stringAProcesar += "1"
    #         while i < numElementos:
    #             numRandom = random.randint(0, 10)
    #             stringAProcesar += "," + str(numRandom)
    #             i += 1
    #     self.assertEqual(Procesador().procesadorText(stringAProcesar), [numElementos, 0, 0, 0], "Arreglo con n números")

    # def test_procesador_String_numero_encontrar_minimo_vacio(self):
    #     listaPrueba = ""
    #     self.assertEqual(Procesador().procesadorText(listaPrueba), [0, -1, 0, 0], "Arreglo vacio")
    #
    # def test_procesador_String_numero_encontrar_minimo_un_numero(self):
    #     listaPrueba = "1"
    #     self.assertEqual(Procesador().procesadorText(listaPrueba), [1, 1, 0, 0], "Arreglo vacio")
    #
    # def test_procesador_String_numero_encontrar_minimo_dos_numero(self):
    #     listaPrueba = "2,3"
    #     self.assertEqual(Procesador().procesadorText(listaPrueba), [2, 2, 0, 0], "Arreglo vacio")
    #
    # def test_procesador_String_numero_encontrar_minimo_n_Numeros(self):
    #     stringAProcesar = "5, 7, 9 , 10, 2, 1"
    #
    #     self.assertEqual(Procesador().procesadorText(stringAProcesar), [6, 1, 0, 0], "Arreglo con n números")

    def test_procesador_String_numero_encontrar_maximo_vacio(self):
        listaPrueba = ""
        self.assertEqual(Procesador().procesadorText(listaPrueba), [0, -1, -1, 0], "Arreglo vacio")

    # def test_procesador_String_numero_encontrar_maximo_un_numero(self):
    #     listaPrueba = "1"
    #     self.assertEqual(Procesador().procesadorText(listaPrueba), [1, 1, 0, 0], "Arreglo vacio")
    #
    # def test_procesador_String_numero_encontrar_maximo_dos_numero(self):
    #     listaPrueba = "2,3"
    #     self.assertEqual(Procesador().procesadorText(listaPrueba), [2, 2, 0, 0], "Arreglo vacio")
    #
    # def test_procesador_String_numero_encontrar_maximo_n_Numeros(self):
    #     stringAProcesar = "5, 7, 9 , 10, 2, 1"
    #
    #     self.assertEqual(Procesador().procesadorText(stringAProcesar), [6, 1, 0, 0], "Arreglo con n números")