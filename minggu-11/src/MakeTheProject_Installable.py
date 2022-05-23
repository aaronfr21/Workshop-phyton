#Describe the Project
##setup.py
"""
from setuptools import find_packages, setup
setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
"""

##MANIFEST.in
"""
include flaskr/schema.sql
graft flaskr/static
graft flaskr/templates
global-exclude *.pyc
"""

#INstall the Project
'''
$ pip install -e .
'''

'''
$ pip list
Package        Version   Location
-------------- --------- ----------------------------------
click          6.7
Flask          1.0
flaskr         1.0.0     /home/user/Projects/flask-tutorial
itsdangerous   0.24
Jinja2         2.10
MarkupSafe     1.0
pip            9.0.3
setuptools     39.0.1
Werkzeug       0.14.1
wheel          0.30.0
'''