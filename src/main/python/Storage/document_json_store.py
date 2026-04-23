from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException
from Storage.json_store import JsonStore
from uc3m_consulting.enterprise_manager_config import TEST_DOCUMENTS_STORE_FILE

class DocumentJsonStore(JsonStore):
    """Almacén especializado para documentos con patrón Singleton"""
    _instance = None  # Instancia única de DocumentJsonStore

    def __new__(cls):
        """Sobrescribir __new__ para asegurar Singleton en esta clase"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if hasattr(self, '__initialized') and self.__initialized:
            return
        super().__init__()
        self._file_name = TEST_DOCUMENTS_STORE_FILE
        self.load_store()
        if hasattr(self, '__initialized'):
            self.__initialized = True

    def find_by_date(self, date_str):
        """Encuentra todos los documentos que coinciden con la fecha dada"""
        matching_documents = []
        for document in self._data_list:
            if "register_date" in document:
                from datetime import datetime
                document_date = datetime.fromtimestamp(document["register_date"]).strftime("%d/%m/%Y")
                if document_date == date_str:
                    matching_documents.append(document)
        return matching_documents

    def add_item(self, item):
        """Añade un nuevo documento al almacén"""
        super().add_item(item)
        self.save_store()
