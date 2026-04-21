"""Módulo: attribute. Contiene la clase base Attribute"""
from abc import ABC, abstractmethod


class Attribute(ABC):
    """Clase base abstracta para todos los atributos de negocio con validación"""

    def __init__(self, value):
        """Inicializa el atributo con un valor y lo valida"""
        self._value = value
        self.validate()

    @abstractmethod
    def validate(self):
        """Valida el valor del atributo. Debe ser implementado por las subclases"""

    @abstractmethod
    def to_json(self):
        """Convierte el atributo a representación JSON. Debe ser implementado por las subclases"""

    def __str__(self):
        """Representación en cadena del atributo"""
        return str(self._value)

    @property
    def value(self):
        """Obtiene el valor del atributo"""
        return self._value
