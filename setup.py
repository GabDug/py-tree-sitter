"""
Py-Tree-sitter
"""

from platform import system

from setuptools import Extension, setup

# Only ext_modules is not supported in pyproject.toml
setup(
    ext_modules=[
        Extension(
            "tree_sitter.binding",
            ["tree_sitter/core/lib/src/lib.c", "tree_sitter/binding.c"],
            include_dirs=["tree_sitter/core/lib/include", "tree_sitter/core/lib/src"],
            extra_compile_args=(
                ["-std=c99", "-Wno-unused-variable"] if system() != "Windows" else None
            ),
        )
    ],
)
