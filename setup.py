
from setuptools import setup

setup(
    name="songDatawebsite",
    version="0.1.0",
    packages=["website"],
    include_package_data=True,
    install_requires=[
        "arrow",
        "bs4",
        "Flask",
        "html5validator",
        "nodeenv",
        "pycodestyle",
        "pydocstyle",
        "pylint",
        "pytest",
        "requests",
        "selenium",
        "psycopg2-binary"
    ],
    python_requires=">=3.6",
)
