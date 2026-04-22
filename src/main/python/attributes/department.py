"""Módulo: department. Contiene la clase Department para validación de departamento"""
from attributes.attribute import Attribute
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException


class Department(Attribute):
    """Clase para validar y almacenar un departamento de proyecto"""

    # Departamentos válidos
    VALID_DEPARTMENTS = {"HR", "FINANCE", "LEGAL", "LOGISTICS"}

    def validate(self):
        """Valida que el departamento sea uno de los valores permitidos"""
        if not isinstance(self._value, str):
            raise EnterpriseManagementException("Invalid department")

        if self._value not in self.VALID_DEPARTMENTS:
            raise EnterpriseManagementException("Invalid department")

    def to_json(self):
        """Convierte el departamento a su representación JSON"""
        return self._value