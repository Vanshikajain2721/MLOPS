from setuptools import find_packages,setup
from typing import List

H_E_D = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]

        if H_E_D in requirements:
            requirements.remove(H_E_D)
    return requirements

setup(
name = 'MLOPS',
version = '0.0.1',
author = 'Vanshika',
author_email = 'vanshika2721@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)