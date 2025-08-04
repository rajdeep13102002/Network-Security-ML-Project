from setuptools import find_packages, setup
from typing import List

requirement_list:List[str]=[]
def get_requirements():
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("Requirements file not found")
    
    return requirement_list

print(get_requirements())

setup(
    name = 'Network Security ML Project',
    version='0.0.1',
    author='Rajdeep Umrani',
    author_email='umranirajdeep13@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements()
)