NAME_OF_PROJECT = 'MyProject' # DEFAULT = 'MyProject'
AUTHOR = 'DEV' # DEFAULT = 'DEV'
VERSION = 'v0.0.1' # DEFAULT = 0.0.1
DESCRIPTION = f'{NAME_OF_PROJECT} {VERSION} by {AUTHOR}' # DESCRIPTION = f'{NAME_OF_PROJECT} {VERSION} by {AUTHOR}'

VENV = 'pyvenv' # VENV = 'pyvenv'
ARCHITURE = 'standart' # ARCHITURE = 'standart'

REPLACE_EXISTS_FILE = False # DEFAULT = False
REPLACE_EXISTS_FOLDERS = False # DEFAULT = False

PATH_FLD = (
'tests', 
'cache', 
'logs', 
'docs',
'src', 
'.git',
'src/tests',
f'src/{NAME_OF_PROJECT}', 
f'src/{NAME_OF_PROJECT}/images', 
f'src/{NAME_OF_PROJECT}/users', 
f'src/{NAME_OF_PROJECT}/products',
f'src/{NAME_OF_PROJECT}/database', 
f'src/{NAME_OF_PROJECT}/utils'
)

PATH_FLE = (
'.gitignore', 
'README.md', 
'pyproject.toml', 
'LICENSE', 
'.env',
'docs/index.md',
'src/tests/__init__.py', 
'src/tests/test_users.py', 
'src/tests/test_products.py', 
f'src/{NAME_OF_PROJECT}/main.py', 
f'src/{NAME_OF_PROJECT}/config.py', 
f'src/{NAME_OF_PROJECT}/__init__.py', 
f'src/{NAME_OF_PROJECT}/users/__init__.py', 
f'src/{NAME_OF_PROJECT}/users/models.py', 
f'src/{NAME_OF_PROJECT}/users/services.py', 
f'src/{NAME_OF_PROJECT}/users/api.py', 
f'src/{NAME_OF_PROJECT}/products/__init__.py', 
f'src/{NAME_OF_PROJECT}/products/models.py', 
f'src/{NAME_OF_PROJECT}/products/services.py', 
f'src/{NAME_OF_PROJECT}/database/__init__.py',
f'src/{NAME_OF_PROJECT}/database/connection.py',
f'src/{NAME_OF_PROJECT}/utils/__init__.py',
f'src/{NAME_OF_PROJECT}/utils/helpers.py'
)

CNST_TXT = '''
venv
logs
cache
.env
.vscode
__pycache__
*.pyc
'''
