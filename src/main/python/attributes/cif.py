"""Módulo: cif. Contiene la clase CIF para validación de CIF"""
import re
from attributes.attribute import Attribute
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException


class CIF(Attribute):
    """Clase para validar y almacenar un número de CIF"""

    @staticmethod
    def _calculate_control_digit(cif_digits):
        """Calcula el dígito de control para un CIF"""
        suma_pares = 0
        suma_impares = 0

        for index, digit in enumerate(cif_digits):
            if index % 2 == 0:  # Posición par (0, 2, 4, 6)
                valor_duplicado = int(digit) * 2
                if valor_duplicado > 9:
                    suma_pares = suma_pares + (valor_duplicado // 10) + (valor_duplicado % 10)
                else:
                    suma_pares = suma_pares + valor_duplicado
            else:  # Posición impar (1, 3, 5)
                suma_impares = suma_impares + int(digit)

        suma_total = suma_pares + suma_impares
        resto = suma_total % 10
        digito_control = 10 - resto

        return 0 if digito_control == 10 else digito_control

    @staticmethod
    def _validate_control_character(organization_type, digito_control, control_character):
        """Valida el carácter de control según el tipo de organización"""
        letras_control = "JABCDEFGHI"

        if organization_type in ('A', 'B', 'E', 'H'):
            if str(digito_control) != control_character:
                raise EnterpriseManagementException("Invalid CIF character control number")
        elif organization_type in ('P', 'Q', 'S', 'K'):
            if letras_control[digito_control] != control_character:
                raise EnterpriseManagementException("Invalid CIF character control letter")
        else:
            raise EnterpriseManagementException("CIF type not supported")

    def validate(self):
        """Valida el formato y el algoritmo de control del CIF"""
        if not isinstance(self._value, str):
            raise EnterpriseManagementException("CIF code must be a string")

        # Validar formato básico del CIF
        cif_pattern = re.compile(r"^[ABCDEFGHJKNPQRSUVW]\d{7}[0-9A-J]$")
        if not cif_pattern.fullmatch(self._value):
            raise EnterpriseManagementException("Invalid CIF format")

        # Extraer componentes del CIF
        organization_type = self._value[0]
        cif_digits = self._value[1:8]
        control_character = self._value[8]

        # Calcular y validar dígito de control
        digito_control = self._calculate_control_digit(cif_digits)
        self._validate_control_character(organization_type, digito_control, control_character)

    def to_json(self):
        """Convierte el CIF a su representación JSON"""
        return self._value
