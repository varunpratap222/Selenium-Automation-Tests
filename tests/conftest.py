# tests/conftest.py
import sys
import os

def pytest_configure():
    # Add the project root directory to the sys.path so that Python can find the 'pages' package
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)