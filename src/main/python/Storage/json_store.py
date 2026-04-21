import json

from src.main.python.uc3m_consulting.enterprise_management_exception import EnterpriseManagementException

class JsonStore:
    _file_name = ""
    _data_list = []
    def __init__(self):
        pass

    def load_store(self ):
        try:
            with open(self._file_name, "r", encoding="utf-8", newline="") as file:
                self._data_list = json.load(file)
        except FileNotFoundError:
            self._data_list = []
        except json.JSONDecodeError as ex:
            raise EnterpriseManagementException("JSON Decode Error - Wrong JSON Format") from ex

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
            raise EnterpriseManagementException("Wrong file  or file path") from ex
        except json.JSONDecodeError as ex:
            raise EnterpriseManagementException("JSON Decode Error - Wrong JSON Format") from ex


    def find_docs(self):
        pass
