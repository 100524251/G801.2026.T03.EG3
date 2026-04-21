from src.main.python.uc3m_consulting.enterprise_management_exception import EnterpriseManagementException
from src.main.python.Storage.json_store import JsonStore
from src.main.python.uc3m_consulting.enterprise_manager_config import PROJECTS_STORE_FILE


class ProjectJsonStore(JsonStore):

    def __init__(self):
        super().__init__()
        self._file_name = PROJECTS_STORE_FILE
        self.load_store()
    def add_item(self, item):
        if self.find_item(item) is not None:
            raise EnterpriseManagementException("Duplicated project in projects list")
        super().add_item(item)