"""Paquete: Storage. Exporta las clases de almacenamiento JSON"""
from Storage.json_store import JsonStore
from Storage.project_json_store import ProjectJsonStore
from Storage.document_json_store import DocumentJsonStore
from Storage.reports_json_store import ReportsJsonStore

__all__ = [
    "JsonStore",
    "ProjectJsonStore",
    "DocumentJsonStore",
    "ReportsJsonStore"
]