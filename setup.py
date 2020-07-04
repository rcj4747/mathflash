"""
A simple math flashcard program
"""
import os

from setuptools import find_packages, setup

reqs_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')

with open(reqs_path, 'r') as req_file:
    dependencies = req_file.readlines()

setup(
    name='mathflash',
    version='0.1.0',
    packages=find_packages(),
    url='',
    license='GPLv3',
    author='Robert C Jennings',
    author_email='rcj4747@gmail.com',
    description='A Math Flash Cards Game',
    long_description=__doc__,
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'mathflash = mathflash:main',
        ],
    },
)
