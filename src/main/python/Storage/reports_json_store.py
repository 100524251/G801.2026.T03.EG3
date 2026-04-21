from src.main.python.uc3m_consulting.enterprise_management_exception import EnterpriseManagementException
from src.main.python.Storage.json_store import JsonStore
from src.main.python.uc3m_consulting.enterprise_manager_config import TEST_NUMDOCS_STORE_FILE


class ReportsJsonStore(JsonStore):

    def __init__(self):
        super().__init__()
        self._file_name = TEST_NUMDOCS_STORE_FILE
        self.load_store()

    def find_by_query_date(self, query_date):
        """Find all reports matching the given query date"""
        matching_reports = []
        for report in self._data_list:
            if "Querydate" in report and report["Querydate"] == query_date:
                matching_reports.append(report)
        return matching_reports

    def add_item(self, item):
        """Add a new report to the store"""
        super().add_item(item)
        self.save_store()
