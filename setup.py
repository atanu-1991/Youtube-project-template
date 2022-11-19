from setuptools import setup

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()


REPO_NAME = "Youtube-project-template"
AUTHOR_USER_NAME = "atanu-1991"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = []

setup(
    name= SRC_REPO,
    version= "0.0.1",
    author= AUTHOR_USER_NAME,
    description= "This is our First Release",
    long_description= long_description,
    url= f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email= "atanukundu1991@gmail.com",
    packages= [SRC_REPO],
    python_requires = ">=3.6",
    install_requires = LIST_OF_REQUIREMENTS
)