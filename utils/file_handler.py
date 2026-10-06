"""
utils/file_handler.py

Educational Concepts:
1. File Handling: open(), read(), write(), with statement (Context Managers)
2. JSON Module: json.load(), json.dump()
3. Error Handling for missing/corrupted files
4. OS module for path operations
"""

import json
import os
from utils.exceptions import StudentManagementError

# CONCEPT: Default path constant
DEFAULT_DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "students.json")


def ensure_directory_exists(file_path: str):
    """
    Ensures that the directory for the specified file path exists.
    
    # CONCEPT: Operating system module path operations
    """
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)


def load_students_from_json(file_path: str = DEFAULT_DATA_PATH) -> list:
    """
    Loads student raw records from a JSON file.
    
    # CONCEPT: File Reading with Context Manager (`with open`)
    # CONCEPT: JSON Decoding (`json.load`)
    # CONCEPT: Exception Handling for FileNotFoundError & json.JSONDecodeError
    """
    ensure_directory_exists(file_path)
    
    if not os.path.exists(file_path):
        print(f"[INFO] Data file '{file_path}' not found. Initializing empty dataset.")
        return []

    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                print(f"[WARNING] Corrupted data structure in '{file_path}'. Expected a list.")
                return []
    except FileNotFoundError:
        print(f"[INFO] File '{file_path}' not found. Starting with empty records.")
        return []
    except json.JSONDecodeError as err:
        print(f"[ERROR] Corrupted JSON in file '{file_path}': {err}. Backup recommended.")
        return []
    except Exception as exc:
        raise StudentManagementError(f"Failed to read data file: {exc}")


def save_students_to_json(student_dicts: list, file_path: str = DEFAULT_DATA_PATH) -> bool:
    """
    Saves student dictionary records to a JSON file.
    
    # CONCEPT: File Writing with Context Manager (`with open`)
    # CONCEPT: JSON Serialization (`json.dump`)
    """
    ensure_directory_exists(file_path)
    
    try:
        with open(file_path, mode='w', encoding='utf-8') as file:
            # CONCEPT: json.dump with indentation for human readability
            json.dump(student_dicts, file, indent=4)
        return True
    except Exception as exc:
        print(f"[ERROR] Failed to save student records to '{file_path}': {exc}")
        return False
