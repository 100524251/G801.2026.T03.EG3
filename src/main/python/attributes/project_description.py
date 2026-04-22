"""Módulo: project_description. Contiene la clase ProjectDescription para validación de descripción"""
import re
from attributes.attribute import Attribute
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException

class ProjectDescription(Attribute):
    """Clase para validar y almacenar una descripción de proyecto"""

    def validate(self):
        """Valida que la descripción tenga entre 10 y 30 caracteres"""
        if not isinstance(self._value, str):
            raise EnterpriseManagementException("Invalid description format")
        # Validar patrón: 10-30 caracteres
        description_pattern = re.compile(r"^.{10,30}$")
        if not description_pattern.fullmatch(self._value):
            raise EnterpriseManagementException("Invalid description format")

    def to_json(self):
        """Convierte la descripción a su representación JSON"""
        return self._value