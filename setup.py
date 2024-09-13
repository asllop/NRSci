from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='NRSci',
    version='0.1.0',
    description='New Relic data importer for Pandas.',
    long_description=readme,
    author='asllop',
    url='https://github.com/asllop/NRSci',
    license=license,
    packages=find_packages()
)