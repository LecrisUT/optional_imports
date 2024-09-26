from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from .importer import Importer

if TYPE_CHECKING:
    from collections.abc import Iterable


pathlib_module = Importer("pathlib")()

## Questioning if this is necessary
# __all__ = pathlib_module.__all__
# def __dir__() -> Iterable[str]:
#     return pathlib_module.__dir__()

sys.modules["optionals.pathlib"] = pathlib_module
