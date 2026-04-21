"""MODULE: enterprise_project. Contains the EnterpriseProject class"""
import hashlib
import json
import re
from datetime import datetime, timezone
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException

class EnterpriseProject:
    """Class representing a project"""
    #pylint: disable=too-many-arguments, too-many-positional-arguments

    @staticmethod
    def validate_cif(company_cif: str):
        """Validates a CIF number."""
        if not isinstance(company_cif, str):
            raise EnterpriseManagementException("CIF code must be a string")
        cif_pattern = re.compile(r"^[ABCDEFGHJKNPQRSUVW]\d{7}[0-9A-J]$")
        if not cif_pattern.fullmatch(company_cif):
            raise EnterpriseManagementException("Invalid CIF format")

        organization_type = company_cif[0]
        cif_digits = company_cif[1:8]
        control_character = company_cif[8]

        even_position_sum = 0
        odd_position_sum = 0

        for index in range(len(cif_digits)):
            if index % 2 == 0:
                doubled_value = int(cif_digits[index]) * 2
                if doubled_value > 9:
                    even_position_sum = even_position_sum + (doubled_value // 10) + (doubled_value % 10)
                else:
                    even_position_sum = even_position_sum + doubled_value
            else:
                odd_position_sum = odd_position_sum + int(cif_digits[index])

        total_sum = even_position_sum + odd_position_sum
        remainder = total_sum % 10
        control_digit = 10 - remainder

        if control_digit == 10:
            control_digit = 0

        control_letters = "JABCDEFGHI"

        if organization_type in ('A', 'B', 'E', 'H'):
            if str(control_digit) != control_character:
                raise EnterpriseManagementException("Invalid CIF character control number")
        elif organization_type in ('P', 'Q', 'S', 'K'):
            if control_letters[control_digit] != control_character:
                raise EnterpriseManagementException("Invalid CIF character control letter")
        else:
            raise EnterpriseManagementException("CIF type not supported")
        return True

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

    @staticmethod
    def validate_starting_date(starting_date):
        """validates the date format using regex"""
        my_date = EnterpriseProject.validate_date_format(starting_date)

        if my_date < datetime.now(timezone.utc).date():
            raise EnterpriseManagementException("Project's date must be today or later.")

        if my_date.year < 2025 or my_date.year > 2050:
            raise EnterpriseManagementException("Invalid date format")
        return starting_date

    @staticmethod
    def validate_project_acronym(project_acronym: str):
        """validates the project acronym format"""
        acronym_pattern = re.compile(r"^[a-zA-Z0-9]{5,10}")
        result = acronym_pattern.fullmatch(project_acronym)
        if not result:
            raise EnterpriseManagementException("Invalid acronym")
        return project_acronym

    @staticmethod
    def validate_project_description(project_description: str):
        """validates the project description format"""
        description_pattern = re.compile(r"^.{10,30}$")
        result = description_pattern.fullmatch(project_description)
        if not result:
            raise EnterpriseManagementException("Invalid description format")
        return project_description

    @staticmethod
    def validate_department(department: str):
        """validates the project department"""
        department_pattern = re.compile(r"(HR|FINANCE|LEGAL|LOGISTICS)")
        result = department_pattern.fullmatch(department)
        if not result:
            raise EnterpriseManagementException("Invalid department")
        return department

    def __init__(self,
                 company_cif: str,
                 project_acronym: str,
                 project_description: str,
                 department: str,
                 starting_date: str,
                 project_budget: float):
        self.__company_cif = company_cif
        self.__project_description = project_description
        self.__project_achronym = project_acronym
        self.__department = department
        self.__starting_date = starting_date
        self.__project_budget = project_budget
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
    def company_cif(self):
        """Company's cif"""
        return self.__company_cif

    @company_cif.setter
    def company_cif(self, value):
        self.__company_cif = value

    @property
    def project_description(self):
        """Project description"""
        return self.__project_description

    @project_description.setter
    def project_description(self, value):
        self.__project_description = value

    @property
    def project_acronym(self):
        """Property representing the type of transfer: REGULAR, INMEDIATE or URGENT """
        return self.__project_achronym
    @project_acronym.setter
    def project_acronym(self, value):
        self.__project_achronym = value

    @property
    def project_budget(self):
        """Property respresenting the transfer amount"""
        return self.__project_budget
    @project_budget.setter
    def project_budget(self, value):
        self.__project_budget = value

    @property
    def department(self):
        """Property representing the transfer concept"""
        return self.__department
    @department.setter
    def department(self, value):
        self.__department = value

    @property
    def starting_date( self ):
        """Property representing the transfer's date"""
        return self.__starting_date
    @starting_date.setter
    def starting_date( self, value ):
        self.__starting_date = value

    @property
    def time_stamp(self):
        """Read-only property that returns the timestamp of the request"""
        return self.__time_stamp

    @property
    def project_id(self):
        """Returns the md5 signature (transfer code)"""
        return hashlib.md5(str(self).encode()).hexdigest()
