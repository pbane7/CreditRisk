from setuptools import find_packages,setup
from typing import List

REQUIREMENT_FILE_NAME = open("requirements.txt","r")

hyphen = "-e ."

def get_requirements()->List[str]:

    req_list = REQUIREMENT_FILE_NAME.read()
    req_list = req_list.split("\n")

    if hyphen in req_list:
        req_list.remove(hyphen)
    else:
        pass
    #assignment: write a code to read requirement.txt file 
    return req_list


setup(

    name="CreditRisk",
    version="0.0.1",
    author="pbane",
    author_email="prathameshbane1605@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),
)