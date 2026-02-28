NAME_OF_PROJECT = 'MyProject' # DEFAULT = 'MyProject'
AUTHOR = 'DEV' # DEFAULT = 'DEV'
VERSION = 'v0.0.1' # DEFAULT = 0.0.1
DESCRIPTION = f'{NAME_OF_PROJECT} {VERSION} by {AUTHOR}' # DEFAULT = f'{NAME_OF_PROJECT} {VERSION} by {AUTHOR}'
LICENSE = 'MIT' # DEFAULT = 'MIT' 
EMAIL = 'youremail@example.com' # DEFAULT = 'youremail@example.com'
HOMEPAGE = f'https://github.com/{AUTHOR}' # Default = f'https://github.com/{AUTHOR}'
REPOSITORY = f'https://github.com/{AUTHOR}/{NAME_OF_PROJECT}' # Default = f'https://github.com/{AUTHOR}/{NAME_OF_PROJECT}'

LANGUAGE = 'py' # DEFAULT = 'py'
VENV = 'pyvenv' # DEFAULT = 'pyvenv'
ARCHITURE = 'standart' # DEFAULT = 'standart'

REPLACE_EXISTS_FILE = False # DEFAULT = False
REPLACE_EXISTS_FOLDERS = False # DEFAULT = False
QUIET_LAUNCH = False # DEFAULT = False 

PATHS_FOLDERS = (
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

PATHS_FILES = (
'.gitignore', 
'README.md', 
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

GITIGNORE = '''venv
logs
cache
.env
.vscode
__pycache__
*.pyc
'''

from datetime import date

MIT = f'''Copyright (c) {date.today().year} {AUTHOR}

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

TOML = {
    "project": {
        "name": NAME_OF_PROJECT,
        "version": VERSION,
        "description": DESCRIPTION,
        "readme": "README.md",
        "requires-python": ">=3.8",
        "license": {"file": "LICENSE"},
        "authors": [{"name": AUTHOR, "email": EMAIL}],
        "urls": {
            "Homepage": HOMEPAGE,
            "Repository": REPOSITORY,
        },
    }
}
