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
            raise EnterpriseManagementException("El departamento debe ser una cadena de texto")
        
        if self._value not in self.VALID_DEPARTMENTS:
            valid_options = ", ".join(sorted(self.VALID_DEPARTMENTS))
            raise EnterpriseManagementException(
                f"Departamento inválido - debe ser uno de: {valid_options}"
            )

    def to_json(self):
        """Convierte el departamento a su representación JSON"""
        return self._value
