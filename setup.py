from setuptools import find_packages, setup
from typing import List

## Constants
HYPHEN_E_DOT = "-e ."

def get_requirements(file_path : str) -> List[str]:
    '''
    This function returns the list of requirements
    '''
    
    requirements = []
    with open(file=file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        ## Note that, when we manually run the setup.py the "-e ." in requirements.txt need not run. So, remove it.
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements 
        

## pip install -r requirements.txt
## when ever we run requirements.txt this set up file should run. To do that, add "-e ." at the end
## of the requirements.txt file.

setup(
    name='student-performance-predictor',
    version='0.0.1',
    author='avsk',
    author_email='avskkrish80@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)