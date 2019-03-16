from setuptools import setup, find_packages

setup(
    name='vnprovinces',
    version='1.0.0',
    url='https://github.com/dduong42/django-vnprovinces.git',
    author='Daniel Duong',
    description="A Django application with Vietnam's provinces/districts/wards",
    packages=find_packages(),    
    install_requires=['Django'],
)
