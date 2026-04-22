"""Paquete: attributes. Exporta todas las clases de atributos de negocio"""
from src.main.python.attributes.attribute import Attribute
from src.main.python.attributes.cif import CIF
from src.main.python.attributes.project_acronym import ProjectAcronym
from src.main.python.attributes.budget import Budget
from src.main.python.attributes.department import Department
from src.main.python.attributes.project_description import ProjectDescription
from src.main.python.attributes.starting_date import StartingDate

__all__ = [
    "Attribute",
    "CIF",
    "ProjectAcronym",
    "Budget",
    "Department",
    "ProjectDescription",
    "StartingDate"
]
