from setuptools import find_package,setup
from typing import List


HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

    return requirements

setup(
    name='RegressorProject',
    version='0.0.1',
    author='Anand',
    author_email='anand.jangir5829@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)