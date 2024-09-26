from optionals.pathlib import pathlib as optional_pathlib
import pathlib as real_pathlib

from typing import reveal_type

if __name__ == "__main__":
    optional_cwd = optional_pathlib.Path(".")
    print(f"optinal_cwd[{type(optional_cwd)}] = {optional_cwd}")
    reveal_type(optional_pathlib)
    reveal_type(optional_cwd)
    real_cwd = real_pathlib.Path(".")
    print(f"real_cwd[{type(real_cwd)}] = {real_cwd}")
    reveal_type(real_pathlib)
    reveal_type(real_cwd)
