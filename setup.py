from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            # .strip() removes leading/trailing whitespace and line terminators (\n, \r\n)
            line = line.strip()
            # Ignore comments, blank lines, and editable installs
            if line and not line.startswith('#') and not line.startswith('-e'):
                requirements.append(line)
    return requirements

setup(
    name = 'my_package',
    version = '0.0.1',
    author = 'Ishika Saha',
    author_email= 'ishika.sahajuly21@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)