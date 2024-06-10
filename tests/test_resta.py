# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import resta

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_resta(self):
        assert resta(4,2) == 2
        assert resta(3,1) == 2
        assert resta(7,5) == 2
        assert resta(3,2) == 1
