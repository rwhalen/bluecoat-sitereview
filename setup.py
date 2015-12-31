from distutils.core import setup
import os
import sys

setup(
    name='bluecoat',  
    version='1.0',
    author='Ryan Whalen',
    author_email='whalen.ryan@gmail.com',
    description='BlueCoat SiteReview query and submission',
    install_requires=[
        'simplejson',
        'requests'
    ],
    py_modules=[
        'src/bluecoat'
    ]
)