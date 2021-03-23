from unittest import TestCase

from Procesador import Procesador
import random


class ProcesadorTest(TestCase):
    def test_procesador_String_numero_elementos_Vacio(self):
        self.assertEqual(Procesador().procesadorText(""), [0, 0, 0, 0], "Arreglo vacío")

    def test_procesador_String_numero_elementos_un_Numero(self):
        self.assertEqual(Procesador().procesadorText("1"), [1, 0, 0, 0], "Arreglo con un número")

    def test_procesador_String_numero_elementos_dos_Numeros(self):
        self.assertEqual(Procesador().procesadorText("1,2"), [2, 0, 0, 0], "Arreglo con un número")

    def test_procesador_String_numero_elementos_n_Numeros(self):
        numElementos = random.randint(3, 10)
        stringAProcesar = ""

        if numElementos >= 1:
            i = 1
            stringAProcesar += "1"
            while i < numElementos:
                numRandom = random.randint(0, 10)
                stringAProcesar += "," + str(numRandom)
                i += 1
        self.assertEqual(Procesador().procesadorText(stringAProcesar), [numElementos, 0, 0, 0], "Arreglo con un número")
