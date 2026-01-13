from setuptools import setup, find_packages
from typing import List
HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str)->list[str]:
    requirements=[]
    with open(file_path) as f:
        requirements=f.read().splitlines()

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="mlprojects",
    version="0.1.0",
    packages=find_packages(),
    author="Nikunj",
    author_email="nikunj@nikunj.com",
    install_requires=get_requirements("requirements.txt")
)
