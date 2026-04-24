"""Module: document_json_store. Specialized JSON store for documents with Singleton pattern"""
from datetime import datetime
from storage.json_store import JsonStore
from uc3m_consulting.enterprise_manager_config import TEST_DOCUMENTS_STORE_FILE


class DocumentJsonStore(JsonStore):
    """Almacén especializado para documentos con patrón Singleton"""

    def __init__(self):
        if self.is_initialized():
            return
        super().__init__()
        self._file_name = TEST_DOCUMENTS_STORE_FILE
        self.load_store()
        self._mark_initialized()

    def find_by_date(self, date_str):
        """Encuentra todos los documentos que coinciden con la fecha dada"""
        matching_documents = []
        for document in self._data_list:
            if "register_date" in document:
                document_date = datetime.fromtimestamp(
                    document["register_date"]
                ).strftime("%d/%m/%Y")
                if document_date == date_str:
                    matching_documents.append(document)
        return matching_documents

    def add_item(self, item):
        """Añade un nuevo documento al almacén"""
        super().add_item(item)
        self.save_store()
