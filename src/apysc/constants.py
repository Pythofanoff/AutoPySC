from .paths import *

GITIGNORE = '''# Byte-compiled / optimized files
__pycache__/
*.py[cod]
*$py.class
*.pyo

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache/
pytest_cache/
.coveragerc
coverage.xml
*.cover
*.py,cover
.pytest_cache/

# Type checkers / linters
.mypy_cache/
.dmypy.json
dmypy.json
.pyre/
.ruff_cache/

# Python version managers
.python-version

# Virtual environments
.venv/
venv/
env/
ENV/
env.bak/
venv.bak/

# Jupyter Notebook
.ipynb_checkpoints/

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# PDM
.pdm.toml
.pdm-python
__pypackages__/

# Hatch
.hatch/

# IDEs and editors
.idea/
.vscode/
*.code-workspace

# Visual Studio Code Python settings
.pyright/
.pyre/

# PyCharm
*.iml

# Sublime Text
*.sublime-project
*.sublime-workspace

# Vim
*.swp
*.swo
*~

# Emacs
*~
\#*\#

# OS files
.DS_Store
Thumbs.db
ehthumbs.db

# Environment variables and secrets
.env
.env.*
!.env.example

# Local configuration
config.local.py
settings.local.py

# Logs
*.log
logs/

# Databases
*.sqlite
*.sqlite3
*.db

# Application-specific temporary files
tmp/
temp/
.cache/

# Uploaded files and generated media
media/
uploads/
staticfiles/

# Local data and notebooks outputs
data/raw/
data/processed/
models/
outputs/

# Docker
.docker/

# macOS
.AppleDouble
.LSOverride

# Windows
Desktop.ini
$RECYCLE.BIN/

# Linux
.directory
'''

from datetime import date

MIT = f'''Copyright (c) {date.today().year} {AUTHOR}

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

ApacheLicenseVersion2 = f'''Copyright {date.today().year} {AUTHOR}

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
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
