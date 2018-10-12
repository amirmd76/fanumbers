from os import path

from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), 'r+', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='fanumbers',
    version='1.0.1',
    description='Library to work with Farsi (Persian) numbers',
    author='AmirMohammad Dehghan',
    author_email='amirmd76@gmail.com',
    url='https://github.com/amirmd76/fanumbers',
    license='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages()
)
