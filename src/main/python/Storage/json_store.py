import json
import threading

from src.main.python.uc3m_consulting.enterprise_management_exception import EnterpriseManagementException

class JsonStore:
    """Clase base para almacenamiento en JSON con patrón Singleton"""
    _file_name = ""
    _data_list = []
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls, *args, **kwargs):
        """Implementa el patrón Singleton con thread-safety (double-check locking)"""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Inicializa el almacén (se ejecuta solo cuando se crea la instancia)"""
        pass

    def load_store(self ):
        try:
            with open(self._file_name, "r", encoding="utf-8", newline="") as file:
                self._data_list = json.load(file)
        except FileNotFoundError:
            self._data_list = []
        except json.JSONDecodeError as ex:
            raise EnterpriseManagementException("Error de decodificación JSON - Formato JSON incorrecto") from ex

    def find_item(self, item: str):
        for candidate in self._data_list:
            if item == candidate:
                return item
        return None

    def add_item(self, item: str):
        self._data_list.append(item)


    def save_store(self):
        try:
            with open(self._file_name, "w", encoding="utf-8", newline="") as file:
                json.dump(self._data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise EnterpriseManagementException("Archivo no encontrado o ruta incorrecta") from ex
        except json.JSONDecodeError as ex:
            raise EnterpriseManagementException("Error de decodificación JSON - Formato JSON incorrecto") from ex


    def find_docs(self):
        pass
