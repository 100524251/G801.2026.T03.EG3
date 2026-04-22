"""Módulo: project_acronym. Contiene la clase ProjectAcronym para validación de acrónimo"""
import re
from attributes.attribute import Attribute
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException


class ProjectAcronym(Attribute):
    """Clase para validar y almacenar un acrónimo de proyecto"""

    def validate(self):
        """Valida que el acrónimo tenga el formato correcto: [a-zA-Z0-9]{5,10}"""
        if not isinstance(self._value, str):
            raise EnterpriseManagementException("Invalid acronym")

        # Validar patrón: 5-10 caracteres alfanuméricos
        acronym_pattern = re.compile(r"^[a-zA-Z0-9]{5,10}$")
        if not acronym_pattern.fullmatch(self._value):
            raise EnterpriseManagementException("Invalid acronym")

    def to_json(self):
        """Convierte el acrónimo a su representación JSON"""
        return self._value