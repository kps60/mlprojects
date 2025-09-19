from setuptools import find_packages,setup
from typing import List

HYFEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function returns the list of the requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if HYFEN_E_DOT in requirements:
            requirements.remove(HYFEN_E_DOT)
    return requirements

setup(
    name='mlprojects',
    version='0.0.1',
    author='krishna pal',
    author_email='krishnapalsinghgohil60@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)