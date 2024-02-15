# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='system-cloner',
    version='0.1.0',
    description='A system cloner cli tool',
    long_description=readme,
    author='DMG TechLabs',
    author_email='dmg.techlabs@gmail.com',
    url='https://github.com/DMG-TechLabs/system-cloner',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
