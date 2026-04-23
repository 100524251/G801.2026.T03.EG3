"""Tests for Singleton pattern implementation"""
import unittest
from unittest import TestCase
from uc3m_consulting import EnterpriseManager
from storage.project_json_store import ProjectJsonStore
from storage.document_json_store import DocumentJsonStore
from storage.reports_json_store import ReportsJsonStore


class TestSingletonPattern(TestCase):
    """Test class for Singleton pattern verification"""

    def test_enterprise_manager_singleton(self):
        """Test that EnterpriseManager returns the same instance (Singleton)"""
        manager1 = EnterpriseManager()
        manager2 = EnterpriseManager()
        
        # Both instances should be the same object in memory
        self.assertIs(manager1, manager2)
        # They should have the same id
        self.assertEqual(id(manager1), id(manager2))

    def test_project_json_store_singleton(self):
        """Test that ProjectJsonStore returns the same instance (Singleton)"""
        store1 = ProjectJsonStore()
        store2 = ProjectJsonStore()
        
        # Both instances should be the same object in memory
        self.assertIs(store1, store2)
        # They should have the same id
        self.assertEqual(id(store1), id(store2))

    def test_document_json_store_singleton(self):
        """Test that DocumentJsonStore returns the same instance (Singleton)"""
        store1 = DocumentJsonStore()
        store2 = DocumentJsonStore()
        
        # Both instances should be the same object in memory
        self.assertIs(store1, store2)
        # They should have the same id
        self.assertEqual(id(store1), id(store2))

    def test_reports_json_store_singleton(self):
        """Test that ReportsJsonStore returns the same instance (Singleton)"""
        store1 = ReportsJsonStore()
        store2 = ReportsJsonStore()
        
        # Both instances should be the same object in memory
        self.assertIs(store1, store2)
        # They should have the same id
        self.assertEqual(id(store1), id(store2))

    def test_multiple_calls_return_same_instance(self):
        """Test that multiple calls to all Singleton classes return the same instances"""
        manager1 = EnterpriseManager()
        manager2 = EnterpriseManager()
        manager3 = EnterpriseManager()
        
        self.assertIs(manager1, manager2)
        self.assertIs(manager2, manager3)
        
        store1 = ProjectJsonStore()
        store2 = ProjectJsonStore()
        store3 = ProjectJsonStore()
        
        self.assertIs(store1, store2)
        self.assertIs(store2, store3)


if __name__ == '__main__':
    unittest.main()
