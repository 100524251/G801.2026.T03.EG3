from src.main.python.uc3m_consulting.enterprise_management_exception import EnterpriseManagementException
from src.main.python.Storage.json_store import JsonStore
from src.main.python.uc3m_consulting.enterprise_manager_config import TEST_DOCUMENTS_STORE_FILE


class DocumentJsonStore(JsonStore):

    def __init__(self):
        super().__init__()
        self._file_name = TEST_DOCUMENTS_STORE_FILE
        self.load_store()

    def find_by_date(self, date_str):
        """Find all documents matching the given date"""
        matching_documents = []
        for document in self._data_list:
            if "register_date" in document:
                from datetime import datetime
                document_date = datetime.fromtimestamp(document["register_date"]).strftime("%d/%m/%Y")
                if document_date == date_str:
                    matching_documents.append(document)
        return matching_documents

    def add_item(self, item):
        """Add a new document to the store"""
        super().add_item(item)
        self.save_store()
