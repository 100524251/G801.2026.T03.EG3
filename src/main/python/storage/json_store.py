"""Module: json_store. Base class for JSON storage with Singleton pattern"""
import json
import threading

from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException


class SingletonMixin:
    """Mixin implementing Singleton pattern for any class"""
    _instances = {}

    def __new__(cls):
        """Singleton implementation per class"""
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
            cls._instances[cls]._initialized = False
        return cls._instances[cls]

    def _mark_initialized(self):
        """Mark this instance as initialized"""
        self._initialized = True

    def is_initialized(self):
        """Check if instance is already initialized"""
        return hasattr(self, '_initialized') and self._initialized


class JsonStore(SingletonMixin):
    """Clase base para almacenamiento en JSON con patrón Singleton"""
    _file_name = ""
    _data_list = []
    _lock = threading.Lock()

    def __init__(self):
        """Inicializa el almacén (se ejecuta solo cuando se crea la instancia)"""

    def load_store(self):
        """Carga el almacén desde el archivo JSON especificado en _file_name"""
        try:
            with open(self._file_name, "r", encoding="utf-8", newline="") as file:
                self._data_list = json.load(file)
        except FileNotFoundError:
            self._data_list = []
        except json.JSONDecodeError as ex:
            msg = "Error de decodificación JSON - Formato JSON incorrecto"
            raise EnterpriseManagementException(msg) from ex

    def find_item(self, item: str):
        """Busca un elemento en el almacén"""
        for candidate in self._data_list:
            if item == candidate:
                return item
        return None

    def add_item(self, item: str):
        """Añade un nuevo elemento al almacén"""
        self._data_list.append(item)

    def save_store(self):
        """Guarda el almacén en el archivo JSON especificado en _file_name"""
        try:
            with open(self._file_name, "w", encoding="utf-8", newline="") as file:
                json.dump(self._data_list, file, indent=2)
        except FileNotFoundError as ex:
            msg = "Archivo no encontrado o ruta incorrecta"
            raise EnterpriseManagementException(msg) from ex
        except json.JSONDecodeError as ex:
            msg = "Error de decodificación JSON - Formato JSON incorrecto"
            raise EnterpriseManagementException(msg) from ex

    def get_data_list(self):
        """Retorna la lista de datos almacenados"""
        return self._data_list