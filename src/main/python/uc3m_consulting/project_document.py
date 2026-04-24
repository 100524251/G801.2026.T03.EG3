"""Module: project_document. Contains the ProjectDocument class."""
from datetime import datetime, timezone
import hashlib
from freezegun import freeze_time
from storage.document_json_store import DocumentJsonStore
from storage.reports_json_store import ReportsJsonStore
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException


class ProjectDocument:
    """Class representing a project document and its integrity data."""

    def __init__(self, project_id: str, file_name):
        self.__alg = "SHA-256"
        self.__type = "PDF"
        self.__project_id = project_id
        self.__file_name = file_name
        justnow = datetime.now(timezone.utc)
        self.__register_date = datetime.timestamp(justnow)

    def to_json(self):
        """Returns the object data in JSON format."""
        return {
            "alg": self.__alg,
            "type": self.__type,
            "project_id": self.__project_id,
            "file_name": self.__file_name,
            "register_date": self.__register_date,
            "document_signature": self.document_signature
        }

    def __signature_string(self):
        """Composes the string used to generate the document signature."""
        return "{alg:" + str(self.__alg) + ",typ:" + str(self.__type) + ",project_id:" + \
               str(self.__project_id) + ",file_name:" + str(self.__file_name) + \
               ",register_date:" + str(self.__register_date) + "}"

    @property
    def project_id(self):
        """Returns the project identifier associated with the document."""
        return self.__project_id

    @project_id.setter
    def project_id(self, value):
        self.__project_id = value

    @property
    def file_name(self):
        """Returns the document file name."""
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    @property
    def register_date(self):
        """Returns the document registration timestamp."""
        return self.__register_date

    @register_date.setter
    def register_date(self, value):
        self.__register_date = value

    @property
    def document_signature(self):
        """Returns the SHA-256 signature of the document."""
        return hashlib.sha256(self.__signature_string().encode()).hexdigest()

    @classmethod
    def calculate_num_docs(cls, date_str: str):
        """
        Calculates the number of valid documents for a specific date.
        Verifies cryptographic integrity of documents and generates a report.
        """
        doc_store = DocumentJsonStore()
        documents_list = doc_store.find_by_date(date_str)
        documents_found = 0

        # Loop to verify documents already filtered by date
        for stored_document in documents_list:
            register_timestamp = stored_document["register_date"]
            document_datetime = datetime.fromtimestamp(register_timestamp, tz=timezone.utc)
            with freeze_time(document_datetime):
                # Rebuild the document under the original timestamp to verify integrity
                project_document = cls(
                    stored_document["project_id"],
                    stored_document["file_name"]
                )
                if project_document.document_signature == \
                        stored_document["document_signature"]:
                    documents_found = documents_found + 1
                else:
                    msg = "Inconsistent document signature"
                    raise EnterpriseManagementException(msg)

        if documents_found == 0:
            raise EnterpriseManagementException("No documents found")

        # Prepare JSON report
        now_str = datetime.now(timezone.utc).timestamp()
        report = {
            "Querydate": date_str,
            "ReportDate": now_str,
            "Numfiles": documents_found
        }

        reports_store = ReportsJsonStore()
        reports_store.add_item(report)

        return documents_found
