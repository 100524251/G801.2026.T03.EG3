"""Module: enterprise_manager. Provides methods for managing enterprise projects."""
from uc3m_consulting.enterprise_project import EnterpriseProject
from uc3m_consulting.project_document import ProjectDocument
from storage.project_json_store import ProjectJsonStore
from storage.json_store import SingletonMixin


class EnterpriseManager(SingletonMixin):
    """Class providing the main operations for managing enterprise projects."""

    def __init__(self):
        if self.is_initialized():
            return
        self._mark_initialized()

    # pylint: disable=too-many-arguments, too-many-positional-arguments
    def register_project(
        self,
        company_cif: str,
        project_acronym: str,
        project_description: str,
        department: str,
        date: str,
        budget: str
    ):
        """Create, validate and store a new enterprise project."""
        new_project = EnterpriseProject(
            company_cif=company_cif,
            project_acronym=project_acronym,
            project_description=project_description,
            department=department,
            starting_date=date,
            project_budget=budget
        )

        project_store = ProjectJsonStore()
        project_store.add_item(new_project.to_json())
        project_store.save_store()
        return new_project.project_id

    def find_docs(self, date_str):
        """
        Generate a report with the number of valid documents for a given date.

        Args:
            date_str: Date to query in DD/MM/YYYY format.

        Returns:
            Number of valid documents found for the given date.

        Raises:
            EnterpriseManagementException: If the date format is invalid or
            if document integrity validation fails.
        """
        EnterpriseProject.validate_date_format(date_str)
        documents_found = ProjectDocument.calculate_num_docs(date_str)
        return documents_found
