from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException
from Storage.json_store import JsonStore
from uc3m_consulting.enterprise_manager_config import TEST_NUMDOCS_STORE_FILE

class ReportsJsonStore(JsonStore):
    """Almacén especializado para reportes con patrón Singleton"""
    _instance = None  # ← Instancia única de ReportsJsonStore

    def __init__(self):
        super().__init__()
        self._file_name = TEST_NUMDOCS_STORE_FILE
        self.load_store()

    def find_by_query_date(self, query_date):
        """Encuentra todos los reportes que coinciden con la fecha de consulta dada"""
        matching_reports = []
        for report in self._data_list:
            if "Querydate" in report and report["Querydate"] == query_date:
                matching_reports.append(report)
        return matching_reports

    def add_item(self, item):
        """Añade un nuevo reporte al almacén"""
        super().add_item(item)
        self.save_store()
