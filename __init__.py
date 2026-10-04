from importlib.metadata import version

__version__ = version("k3math")

from .mth import Matrix, Polynomial, Vector

__all__ = [
    "Matrix",
    "Polynomial",
    "Vector",
]
