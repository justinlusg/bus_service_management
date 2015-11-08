# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='bus_service_management',
    version=version,
    description='Created for Dynacle Transportation and Workshop Pte Ltd',
    author='AG Technologies Pte Ltd',
    author_email='info@agtech.com.sg',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
