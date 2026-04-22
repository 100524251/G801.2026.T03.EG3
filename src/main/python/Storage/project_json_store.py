from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException
from Storage.json_store import JsonStore
from uc3m_consulting.enterprise_manager_config import PROJECTS_STORE_FILE

class ProjectJsonStore(JsonStore):
    """Almacén especializado para proyectos con patrón Singleton"""
    _instance = None  # ← Instancia única de ProjectJsonStore

    def __init__(self):
        super().__init__()
        self._file_name = PROJECTS_STORE_FILE
        self.load_store()
    
    def add_item(self, item):
        if self.find_item(item) is not None:
            raise EnterpriseManagementException("Duplicated project in projects list")
        super().add_item(item)