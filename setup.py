from setuptools import find_packages, setup
from typing import List 

hyphen_dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    """this function returns list of required packages"""
    requiremnts = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n','') for req in requirements] 
        if hyphen_dot in requirements:
            requirements.remove(hyphen_dot)

    return requirements
setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Jay Patel',
    author_email='jayppatel3627@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)