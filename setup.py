# It will help my machine learning application to make as a package.

from setuptools import find_packages,setup
from typing import List
# metadata of te ML Project
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    ''' This function wil return the list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
name='mlproject',
version='0.0.1',
author='Sriram',
author_email='prskumar1999@gmail.com',
packages=find_packages(),
# install_requires=['pandas','numpy','seaborn']
install_requires=get_requirements('requirements.txt')
)