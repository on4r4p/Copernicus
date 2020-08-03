#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
 

setup(

    name='copernicus',

    version = '2.0.7',

    packages=find_packages(),
    author="Soroboruo",

    author_email="Soroboruo@mail2developer.com",

    description="Osint Tool to get infos about peoples",

    long_description=open('README.md').read(),

    install_requires= ['beautifulsoup4','selenium','neo4jrestclient == 2.1.1','pyfiglet == 0.7.5','Pillow == 3.1.2','transliterate == 1.9','pytesseract == 0.1.6','grapefruit == 0.1a4','fabulous == 0.3.0','PyPDF2 == 1.26.0','dnspython3 == 1.15.0','Unidecode == 0.4.19'],

    include_package_data=True,

    url='https://github.com/Soroboruo/Copernicus',

    scripts=["Copernicus/copernicus.py","Copernicus/imageGwall.py"],

    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "License :: Free for non-commercial use",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.4",
        "Topic :: Utilities",
    ],
 
 
)
