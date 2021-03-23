from unittest import TestCase

from Procesador import Procesador


class ProcesadorTest(TestCase):
    def test_procesador_String_Vacio(self):
        self.assert_(Procesador().procesadorText(""), [0, -1, -1, -1], "Arreglo vacío")
