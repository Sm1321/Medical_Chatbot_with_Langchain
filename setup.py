from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "RAG Medcal Chatbot",
    version = "0.1",
    author =  "Mohan",
    packages = find_packages(),
    install_requires = requirements,
)