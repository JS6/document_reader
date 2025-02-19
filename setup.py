from setuptools import setup, find_packages

with open("requirements.txt") as req_file:
    requirements = req_file.read().split()

print(requirements)

setup(
    name="cacib",
    version="0.0.0",
    description="",
    author="sa-jo",
    packages=find_packages(),
    include_package_data=True,
    install_requirements=requirements,  # Add this line to specify dependencies
)
