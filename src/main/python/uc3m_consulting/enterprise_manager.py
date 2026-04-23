"""Module """
from uc3m_consulting.enterprise_project import EnterpriseProject
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException
from uc3m_consulting.project_document import ProjectDocument
from Storage.project_json_store import ProjectJsonStore

class EnterpriseManager:
    """Class for providing the methods for managing the orders"""
    
    # 1. Clase interna privada
    class __EnterpriseManager:
        """Internal singleton class"""
        def __init__(self):
            pass

    # 2. Atributo estático para guardar la instancia única
    __instance = None

    # 3. Sobreescribir __new__ para implementar el Singleton
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True

    #pylint: disable=too-many-arguments, too-many-positional-arguments
    def register_project(self,
                         company_cif: str,
                         project_acronym: str,
                         project_description: str,
                         department: str,
                         date: str,
                         budget: str):
        """registers a new project"""
        new_project = EnterpriseProject(company_cif=company_cif,
                                        project_acronym=project_acronym,
                                        project_description=project_description,
                                        department=department,
                                        starting_date=date,
                                        project_budget=budget)

        project_store = ProjectJsonStore()
        project_store.add_item(new_project.to_json())
        project_store.save_store()
        return new_project.project_id

    def find_docs(self, date_str):
        """
        Generates a JSON report counting valid documents for a specific date.

        Args:
            date_str (str): date to query.

        Returns:
            number of documents found if report is successfully generated and saved.

        Raises:
            EnterpriseManagementException: On invalid date, integrity failure, or no documents found.
        """
        EnterpriseProject.validate_date_format(date_str)
        documents_found = ProjectDocument.calculate_num_docs(date_str)
        return documents_found
