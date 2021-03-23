from unittest import TestCase

from Procesador import Procesador


class ProcesadorTest(TestCase):
    def test_procesador_String_numero_elementos_Vacio(self):
        self.assertEqual(Procesador().procesadorText(""), [0, 0, 0, 0], "Arreglo vacío")

    def test_procesador_String_numero_elementos_un_Numero(self):
        self.assertEqual(Procesador().procesadorText("1"), [1, 0, 0, 0], "Arreglo con un número")

    def test_procesador_String_numero_elementos_dos_Numeros(self):
        self.assertEqual(Procesador().procesadorText("1,2"), [2, 0, 0, 0], "Arreglo con un número")

