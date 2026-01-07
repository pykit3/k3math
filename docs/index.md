# k3math

[![Action-CI](https://github.com/pykit3/k3math/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3math/actions/workflows/python-package.yml)
[![Documentation Status](https://readthedocs.org/projects/k3math/badge/?version=stable)](https://k3math.readthedocs.io/en/stable/?badge=stable)
[![Package](https://img.shields.io/pypi/pyversions/k3math)](https://pypi.org/project/k3math)

A toy math implementation with Vector, Matrix, and Polynomial classes for basic linear algebra operations.

k3math is a component of [pykit3](https://github.com/pykit3) project: a python3 toolkit set.

## Installation

```bash
pip install k3math
```

## Quick Start

```python
from k3math import Vector, Matrix, Polynomial

# Vector operations
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print(v1 + v2)        # [5.0, 7.0, 9.0]
print(v1 * 2)         # [2.0, 4.0, 6.0]
print(v1.inner_product(v2))  # 32.0

# Matrix operations
m = Matrix([
    [1, 2],
    [3, 4]
])
print(m.determinant())  # -2.0
print(m.solve([5, 11])) # [1.0, 2.0] (solves x + 2y = 5, 3x + 4y = 11)

# Polynomial curve fitting
xs = [1, 2, 3, 4, 5]
ys = [2.1, 4.0, 5.9, 8.1, 10.0]
poly = Polynomial.fit(xs, ys, degree=1)
print(poly)  # Displays the fitted polynomial
```

## API Reference

::: k3math

## License

The MIT License (MIT) - Copyright (c) 2015 Zhang Yanpo (张炎泼)
