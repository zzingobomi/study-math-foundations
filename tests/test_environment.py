"""환경 점검: 실습에 쓰는 패키지와 mymath를 불러올 수 있는지 확인한다."""


def test_packages_import():
    import matplotlib  # noqa: F401
    import numpy  # noqa: F401
    import pandas  # noqa: F401
    import scipy  # noqa: F401
    import sklearn  # noqa: F401
    import statsmodels  # noqa: F401
    import sympy  # noqa: F401


def test_mymath_import():
    import mymath  # noqa: F401
