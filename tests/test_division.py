# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import division

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_division(self):
        assert division(4,2) == 2
        assert division(6,3) == 2
        assert division(20,5) == 4
        assert division(10,2) == 5
