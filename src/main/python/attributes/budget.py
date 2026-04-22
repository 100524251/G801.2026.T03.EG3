"""Módulo: budget. Contiene la clase Budget para validación de presupuesto"""
from src.main.python.attributes.attribute import Attribute
from src.main.python.uc3m_consulting.enterprise_management_exception import EnterpriseManagementException


class Budget(Attribute):
    """Clase para validar y almacenar un presupuesto de proyecto"""

    def validate(self):
        """Valida que el presupuesto esté en el rango [50000, 1000000] con máximo 2 decimales"""
        try:
            budget_value = float(self._value)
        except (ValueError, TypeError):
            raise EnterpriseManagementException("El presupuesto debe ser un número válido")
        
        # Validar rango
        if budget_value < 50000 or budget_value > 1000000:
            raise EnterpriseManagementException("Presupuesto inválido - debe estar entre 50000 y 1000000")
        
        # Validar máximo 2 decimales
        if not self._has_max_decimals(budget_value, 2):
            raise EnterpriseManagementException("Presupuesto inválido - máximo 2 decimales permitidos")

    @staticmethod
    def _has_max_decimals(value, max_decimals):
        """Verifica que un número tenga como máximo el número especificado de decimales"""
        value_str = str(value)
        if '.' in value_str:
            decimal_part = value_str.split('.')[1]
            return len(decimal_part) <= max_decimals
        return True

    def to_json(self):
        """Convierte el presupuesto a su representación JSON"""
        return float(self._value)
