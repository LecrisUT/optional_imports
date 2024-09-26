from __future__ import annotations

import importlib
from types import ModuleType

class Importer:
    def __init__(self, name: str):
        self._name = name
    def __call__(self) -> ModuleType:
        return importlib.import_module(self._name)
