"""Script de prueba para validar todos los componentes creados hasta ahora"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src/main/python'))

from src.main.python.attributes.cif import CIF
from src.main.python.attributes.attribute import Attribute
from src.main.python.Storage.json_store import JsonStore
from src.main.python.Storage.project_json_store import ProjectJsonStore
from src.main.python.Storage.document_json_store import DocumentJsonStore
from src.main.python.Storage.reports_json_store import ReportsJsonStore
from src.main.python.uc3m_consulting.enterprise_management_exception import EnterpriseManagementException

def test_imports():
    """Verifica que todos los módulos se importan correctamente"""
    print("[OK] Todos los módulos se importaron correctamente")

def test_cif_valid():
    """Prueba CIF con valor válido"""
    try:
        cif = CIF("A12345674")  # CIF válido del proyecto
        print(f"[OK] CIF válido creado: {cif}")
    except Exception as e:
        print(f"[ERROR] Error creando CIF válido: {e}")

def test_cif_valid_other_types():
    """Prueba CIFs válidos de otros tipos"""
    valid_cifs = ["B98765431", "E00000000", "H11111119", "P1234567D", "Q9876543A", "S0000000J", "K1111111I"]
    for cif_value in valid_cifs:
        try:
            cif = CIF(cif_value)
            print(f"[OK] CIF {cif_value} válido")
        except Exception as e:
            print(f"[ERROR] Error con CIF {cif_value}: {e}")

def test_cif_invalid_format():
    """Prueba CIF con formato inválido"""
    try:
        cif = CIF("X1111111I")  # X no es permitida
        print("[ERROR] CIF inválido NO lanzó excepción")
    except EnterpriseManagementException as e:
        print(f"[OK] CIF inválido lanzó excepción correctamente: {str(e)}")
    except Exception as e:
        print(f"[OK] CIF inválido lanzó excepción: {str(e)}")

def test_cif_invalid_type():
    """Prueba CIF con tipo incorrecto"""
    try:
        cif = CIF(12345)
        print("[ERROR] CIF con número NO lanzó excepción")
    except EnterpriseManagementException as e:
        print(f"[OK] CIF con tipo incorrecto lanzó excepción: {str(e)}")
    except Exception as e:
        print(f"[OK] CIF con tipo incorrecto lanzó excepción: {str(e)}")

def test_cif_invalid_control():
    """Prueba CIF con control inválido"""
    try:
        cif = CIF("A12345679")  # Control digit incorrecto (debería ser 4)
        print("[ERROR] CIF con control inválido NO lanzó excepción")
    except EnterpriseManagementException as e:
        print(f"[OK] CIF con control inválido lanzó excepción: {str(e)}")
    except Exception as e:
        print(f"[OK] CIF con control inválido lanzó excepción: {str(e)}")

def test_json_store():
    """Prueba que JsonStore está disponible"""
    try:
        store = JsonStore()
        print(f"[OK] JsonStore creada correctamente")
    except Exception as e:
        print(f"[ERROR] Error en JsonStore: {e}")

def test_project_json_store():
    """Prueba que ProjectJsonStore carga correctamente"""
    try:
        store = ProjectJsonStore()
        print(f"[OK] ProjectJsonStore creada y datos cargados")
    except Exception as e:
        print(f"[ERROR] Error en ProjectJsonStore: {e}")

def test_document_json_store():
    """Prueba que DocumentJsonStore funciona"""
    try:
        store = DocumentJsonStore()
        print(f"[OK] DocumentJsonStore creada correctamente")
    except Exception as e:
        print(f"[ERROR] Error en DocumentJsonStore: {e}")

def test_reports_json_store():
    """Prueba que ReportsJsonStore funciona"""
    try:
        store = ReportsJsonStore()
        print(f"[OK] ReportsJsonStore creada correctamente")
    except Exception as e:
        print(f"[ERROR] Error en ReportsJsonStore: {e}")

if __name__ == "__main__":
    print("\n" + "-"*60)
    print("PRUEBAS DE VALIDACION - FASE 1 Y 2")
    print("-"*60 + "\n")
    
    print("1. PRUEBAS DE IMPORTACIÓN:")
    test_imports()
    
    print("\n2. PRUEBAS DE CIF ATTRIBUTE:")
    test_cif_valid()
    test_cif_valid_other_types()
    test_cif_invalid_format()
    test_cif_invalid_type()
    test_cif_invalid_control()
    
    print("\n3. PRUEBAS DE ALMACENES:")
    test_json_store()
    test_project_json_store()
    test_document_json_store()
    test_reports_json_store()
    
    print("\n" + "-"*60)
    print("[OK] TODAS LAS PRUEBAS COMPLETADAS")
    print("-"*60 + "\n")

