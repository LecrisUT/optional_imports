from __future__ import annotations

import importlib
from typing import cast, Generic, TypeVar
from types import ModuleType

ModuleT = TypeVar("ModuleT", bound=ModuleType)
class Importer(Generic[ModuleT]):
    def __init__(self, name: str):
        self._name = name
    def __call__(self) -> ModuleT:
        module = importlib.import_module(self._name)
        # return module
        return cast(ModuleT, module)
