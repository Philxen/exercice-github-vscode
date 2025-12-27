# Ahora esta cagada funciona un poco mejor

import sys
from pathlib import Path

project_root = Path("/home/felipeelocance/exercice-github-vscode")
sys.path.insert(0, str(project_root))

from src.utils import dire_bonjour

def test_dire_bonjour():
    dire_bonjour("Test")

test_dire_bonjour()