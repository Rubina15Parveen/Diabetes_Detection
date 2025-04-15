from setuptools import find_packages, setup
from typing import List 

HYPEN_E = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    Returns a list of required packages to be installed

    '''
    requirements = []
    with open(file_path,'r') as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)
    return requirements




setup(
    name='Diabetes Prediction', 
    version='0.0.1',
    author='Rubina Parveen', 
    author_email='rubina15parveen@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)