#Build and Install
'''
$ pip install wheel
$ pip install flaskr-1.0.0-py3-none-any.whl
'''

##Bash
'''
$ export FLASK_APP=flaskr
$ flask init-db
'''

##Fish
'''
$ set -x FLASK_APP flaskr
$ flask init-db
'''

##CMD
'''
> set FLASK_APP=flaskr
> flask init-db
'''

##Powershell
'''
> $env:FLASK_APP = "flaskr"
> flask init-db
'''

#Configure the Secret Key
'''
$ python -c 'import secrets; print(secrets.token_hex())'
'192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
'''

##venv/var/flaskr-instance/config.py
"""
SECRET_KEY = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
"""

#Run with a Production Server
'''
$ pip install waitress
$ waitress-serve --call 'flaskr:create_app'
'''