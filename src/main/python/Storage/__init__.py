"""Paquete: Storage. Exporta las clases de almacenamiento JSON"""
from storage.json_store import JsonStore
from storage.project_json_store import ProjectJsonStore
from storage.document_json_store import DocumentJsonStore
from storage.reports_json_store import ReportsJsonStore

__all__ = [
    "JsonStore",
    "ProjectJsonStore",
    "DocumentJsonStore",
    "ReportsJsonStore"
]
