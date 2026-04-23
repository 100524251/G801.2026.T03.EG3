"""MODULE: enterprise_project. Contains the EnterpriseProject class"""
import hashlib
import json
import re
from datetime import datetime, timezone
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException
from attributes.cif import CIF
from attributes.project_acronym import ProjectAcronym
from attributes.project_description import ProjectDescription
from attributes.department import Department
from attributes.starting_date import StartingDate
from attributes.budget import Budget

class EnterpriseProject:
    """Class representing a project"""
    #pylint: disable=too-many-arguments, too-many-positional-arguments

    @staticmethod
    def validate_date_format(date_text: str):
        """validates the date format and returns the parsed date"""
        date_pattern = re.compile(r"^(([0-2]\d|3[0-1])\/(0\d|1[0-2])\/\d\d\d\d)$")
        result = date_pattern.fullmatch(date_text)
        if not result:
            raise EnterpriseManagementException("Invalid date format")

        try:
            return datetime.strptime(date_text, "%d/%m/%Y").date()
        except ValueError as ex:
            raise EnterpriseManagementException("Invalid date format") from ex

    def __init__(self,
                 company_cif: str,
                 project_acronym: str,
                 project_description: str,
                 department: str,
                 starting_date: str,
                 project_budget: float):
        self.__company_cif = CIF(company_cif).value
        self.__project_description = ProjectDescription(project_description).value
        self.__project_achronym = ProjectAcronym(project_acronym).value
        self.__department = Department(department).value
        self.__starting_date = StartingDate(starting_date).value
        self.__project_budget = Budget(project_budget).value
        justnow = datetime.now(timezone.utc)
        self.__time_stamp = datetime.timestamp(justnow)

    def __str__(self):
        return "Project:" + json.dumps(self.__dict__)

    def to_json(self):
        """returns the object information in json format"""
        return {
            "company_cif": self.__company_cif,
            "project_description": self.__project_description,
            "project_acronym": self.__project_achronym,
            "project_budget": self.__project_budget,
            "department": self.__department,
            "starting_date": self.__starting_date,
            "time_stamp": self.__time_stamp,
            "project_id": self.project_id
        }

    @property
    def project_id(self):
        """Returns the md5 signature (transfer code)"""
        return hashlib.md5(str(self).encode()).hexdigest()
