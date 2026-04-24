"""Module: project_json_store. Specialized JSON store for projects with Singleton pattern"""
from storage.json_store import JsonStore
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException
from uc3m_consulting.enterprise_manager_config import PROJECTS_STORE_FILE


class ProjectJsonStore(JsonStore):
    """Almacén especializado para proyectos con patrón Singleton"""

    def __init__(self):
        if self.is_initialized():
            return
        super().__init__()
        self._file_name = PROJECTS_STORE_FILE
        self.load_store()
        self._mark_initialized()

    def add_item(self, item):
        """Añade un nuevo proyecto al almacén si no está duplicado"""
        if self.find_item(item) is not None:
            raise EnterpriseManagementException("Duplicated project in projects list")
        super().add_item(item)
