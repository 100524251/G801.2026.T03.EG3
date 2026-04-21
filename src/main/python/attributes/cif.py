"""Módulo: cif. Contiene la clase CIF para validación de CIF"""
import re
from src.main.python.attributes.attribute import Attribute
from src.main.python.uc3m_consulting.enterprise_management_exception import EnterpriseManagementException


class CIF(Attribute):
    """Clase para validar y almacenar un número de CIF"""

    def validate(self):
        """Valida el formato y el algoritmo de control del CIF"""
        if not isinstance(self._value, str):
            raise EnterpriseManagementException("El código CIF debe ser una cadena de texto")
        
        # Validar formato básico del CIF
        cif_pattern = re.compile(r"^[ABCDEFGHJKNPQRSUVW]\d{7}[0-9A-J]$")
        if not cif_pattern.fullmatch(self._value):
            raise EnterpriseManagementException("Formato de CIF inválido")

        # Extraer componentes del CIF
        organization_type = self._value[0]
        cif_digits = self._value[1:8]
        control_character = self._value[8]

        # Calcular suma de posiciones pares e impares
        suma_pares = 0
        suma_impares = 0

        for index in range(len(cif_digits)):
            if index % 2 == 0:  # Posición par (0, 2, 4, 6)
                valor_duplicado = int(cif_digits[index]) * 2
                if valor_duplicado > 9:
                    suma_pares = suma_pares + (valor_duplicado // 10) + (valor_duplicado % 10)
                else:
                    suma_pares = suma_pares + valor_duplicado
            else:  # Posición impar (1, 3, 5)
                suma_impares = suma_impares + int(cif_digits[index])

        # Calcular dígito de control
        suma_total = suma_pares + suma_impares
        resto = suma_total % 10
        digito_control = 10 - resto

        if digito_control == 10:
            digito_control = 0

        # Validar según el tipo de organización
        letras_control = "JABCDEFGHI"

        if organization_type in ('A', 'B', 'E', 'H'):
            # Estos tipos usan dígito de control
            if str(digito_control) != control_character:
                raise EnterpriseManagementException("Número de control de carácter CIF inválido")
        elif organization_type in ('P', 'Q', 'S', 'K'):
            # Estos tipos usan letra de control
            if letras_control[digito_control] != control_character:
                raise EnterpriseManagementException("Letra de control de carácter CIF inválida")
        else:
            raise EnterpriseManagementException("Tipo de CIF no soportado")

    def to_json(self):
        """Convierte el CIF a su representación JSON"""
        return self._value
