"""Module: reports_json_store. Specialized JSON store for reports with Singleton pattern"""
from storage.json_store import JsonStore
from uc3m_consulting.enterprise_manager_config import TEST_NUMDOCS_STORE_FILE


class ReportsJsonStore(JsonStore):
    """Almacén especializado para reportes con patrón Singleton"""

    def __init__(self):
        if self.is_initialized():
            return
        super().__init__()
        self._file_name = TEST_NUMDOCS_STORE_FILE
        self.load_store()
        self._mark_initialized()

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
