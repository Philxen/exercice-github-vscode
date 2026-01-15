# Ahora esta cagada funciona un poco mejor

import sys
from pathlib import Path

project_root = Path("/home/felipeelocance/exercice-github-vscode")
sys.path.insert(0, str(project_root))

from src.utils import dire_bonjour, dire_puteada

def test_dire_bonjour():
    dire_bonjour("Test")

def test_dire_puteada():
    dire_puteada("Test2")

test_dire_puteada()