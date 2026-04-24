"""class for testing the regsiter_order method"""
import unittest
import json
import os.path
import hashlib
from unittest import TestCase
from os import remove
from datetime import datetime, timezone
from freezegun import freeze_time
from uc3m_consulting import (TEST_NUMDOCS_STORE_FILE,
                        EnterpriseManager,
                        EnterpriseManagementException)

class TestTransferRequestTest(TestCase):
    """Class for testing deliver_product"""
    def setUp(self):
        """ inicializo el entorno de prueba """
        if os.path.exists(TEST_NUMDOCS_STORE_FILE):
            remove(TEST_NUMDOCS_STORE_FILE)

    @staticmethod
    def read_file():
        """ this method read a Json file and return the value """
        my_file= TEST_NUMDOCS_STORE_FILE
        try:
            with open(my_file, "r", encoding="utf-8", newline="") as file:
                data = json.load(file)
        except FileNotFoundError as ex:
            raise EnterpriseManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise EnterpriseManagementException("JSON Decode Error - Wrong JSON Format") from ex
        return data


    #pylint: disable=too-many-locals
    @freeze_time("2026/12/31 13:00:00")
    def test_valid_date(self):
        """validates a valid case with a valid date finding documents
        and updating the numdocs_store.json file"""
        mngr = EnterpriseManager()
        res = mngr.find_docs("05/04/2026")
        self.assertEqual(2,res)
        data = self.read_file()
        data_found = False
        for report in data:
            if (report["Querydate"] == "05/04/2026" and
                    report["ReportDate"] == datetime.now(timezone.utc).timestamp() and
                    report["Numfiles"] == 2):
                data_found = True
        self.assertTrue(data_found)

    @freeze_time("2026/12/31 13:00:00")
    def test_file_wrong_date(self):
        """path with wrong cif code (exception)"""
        mngr = EnterpriseManager()

        if os.path.isfile(TEST_NUMDOCS_STORE_FILE):
            with open(TEST_NUMDOCS_STORE_FILE, "r", encoding="utf-8", newline="") as file_org:
                hash_original = hashlib.md5(str(file_org).encode()).hexdigest()
        else:
            hash_original = ""

        with self.assertRaises(EnterpriseManagementException) as cm_obj:
            mngr.find_docs("/04/2026")
        self.assertEqual("Invalid date format",cm_obj.exception.message)

        if os.path.isfile(TEST_NUMDOCS_STORE_FILE):
            with open(TEST_NUMDOCS_STORE_FILE, "r", encoding="utf-8", newline="") as file:
                hash_new = hashlib.md5(str(file).encode()).hexdigest()
        else:
            hash_new = ""
        self.assertEqual(hash_new, hash_original)

    @freeze_time("2026/12/31 13:00:00")
    def test_report_not_found(self):
        """path with wrong cif code (exception)"""
        mngr = EnterpriseManager()

        if os.path.isfile(TEST_NUMDOCS_STORE_FILE):
            with open(TEST_NUMDOCS_STORE_FILE, "r", encoding="utf-8", newline="") as file_org:
                hash_original = hashlib.md5(str(file_org).encode()).hexdigest()
        else:
            hash_original = ""

        with self.assertRaises(EnterpriseManagementException) as cm_obj:
            mngr.find_docs("01/04/2025")
        self.assertEqual("No documents found",cm_obj.exception.message)

        if os.path.isfile(TEST_NUMDOCS_STORE_FILE):
            with open(TEST_NUMDOCS_STORE_FILE, "r", encoding="utf-8", newline="") as file:
                hash_new = hashlib.md5(str(file).encode()).hexdigest()
        else:
            hash_new = ""
        self.assertEqual(hash_new, hash_original)

    @freeze_time("2026/12/31 13:00:00")
    def test_find_by_date(self):
        """Test DocumentJsonStore.find_by_date method"""
        # pylint: disable=import-outside-toplevel
        from storage.document_json_store import DocumentJsonStore

        doc_store = DocumentJsonStore()

        # Search for documents from 05/04/2026 (should find 2 documents)
        matching_docs = doc_store.find_by_date("05/04/2026")
        self.assertEqual(len(matching_docs), 2)

        # Verify that all returned documents have the correct date
        for doc in matching_docs:
            doc_date = datetime.fromtimestamp(doc["register_date"]).strftime("%d/%m/%Y")
            self.assertEqual(doc_date, "05/04/2026")

        # Search for a date with no documents (should return empty list)
        no_docs = doc_store.find_by_date("01/01/2025")
        self.assertEqual(len(no_docs), 0)


if __name__ == '__main__':
    unittest.main()
