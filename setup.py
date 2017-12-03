# coding: utf-8

"""
    bl-db-product

    This is a API document for Product DB

    OpenAPI spec version: 0.0.1
    Contact: master@bluehack.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "stylelens-product"
VERSION = "1.0.18"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="bl-db-product",
    author_email="master@bluehack.net",
    url="",
    keywords=["Swagger", "bl-db-product"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This is a API document for Product DB
    """
)
