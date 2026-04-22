"""Módulo: starting_date. Contiene la clase StartingDate para validación de fecha de inicio"""
import re
from datetime import datetime, timezone
from src.main.python.attributes.attribute import Attribute
from src.main.python.uc3m_consulting.enterprise_management_exception import EnterpriseManagementException


class StartingDate(Attribute):
    """Clase para validar y almacenar una fecha de inicio de proyecto"""

    def validate(self):
        """Valida que la fecha tenga formato DD/MM/YYYY, sea futura y el año esté en [2025, 2050]"""
        if not isinstance(self._value, str):
            raise EnterpriseManagementException("La fecha debe ser una cadena de texto")
        
        # Validar formato DD/MM/YYYY
        date_pattern = re.compile(r"^(([0-2]\d|3[0-1])\/(0\d|1[0-2])\/\d\d\d\d)$")
        if not date_pattern.fullmatch(self._value):
            raise EnterpriseManagementException("Formato de fecha inválido - debe ser DD/MM/YYYY")
        
        # Parsear fecha
        try:
            parsed_date = datetime.strptime(self._value, "%d/%m/%Y").date()
        except ValueError as ex:
            raise EnterpriseManagementException("Fecha inválida") from ex
        
        # Validar que sea futura (>= hoy)
        today = datetime.now(timezone.utc).date()
        if parsed_date < today:
            raise EnterpriseManagementException("La fecha de inicio debe ser hoy o posterior")
        
        # Validar rango de años [2025, 2050]
        if parsed_date.year < 2025 or parsed_date.year > 2050:
            raise EnterpriseManagementException("El año debe estar entre 2025 y 2050")

    def to_json(self):
        """Convierte la fecha a su representación JSON"""
        return self._value
