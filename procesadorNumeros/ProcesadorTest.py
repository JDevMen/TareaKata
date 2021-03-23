from unittest import TestCase

from Procesador import Procesador


class ProcesadorTest(TestCase):
    def test_procesador_String_Vacio(self):
        self.assertEqual(Procesador().procesadorText(""), [0, 0, 0, 0], "Arreglo vacío")
