`<DESCRIPTION>`
 
v. of lib: 0.0.1

 AutoPySC or Auto Python Structure Creator - 
 This is a lightweight, simple library for creating a project tree.

 This library was originally written for my own small, private projects, 
but I decided to keep it publicly available. 
Perhaps one day this small script will grow into something bigger.

Creates the following structure:

```
MyProject
├───.git
├───cache
├───docs
│   └───index.md
├───logs
├───src
│   └───MyProject
│       └───database
│            └───__init__.py
│            └───connection.py
│       └───images
│       └───products
│            └───__init__.py
│            └───models.py
│            └───services.py
│       └───users
│            └───__init__.py
│            └───api.py
│            └───models.py
│            └───services.py
│       └───utils
│            └───__init__.py
│            └───helpers.py
├───tests
│   └───__init__.py
│   └───test_products.py
│   └───test_users.py
└───venv
└───.gitignore
└───LICENCE
└───pyproject.toml
└───README.MD
```
Time of the structure creation: ~±500 ms

`<HOW TO LAUNCH?>`
 1) In terminal: ```pip install APySC```
 
 or:

 Folder APySC, transport along the path:     ```.\python\python38-32\lib\site-packages```
 
 2) In terminal: ```cd MyProject```
 
 3) In terminal: ```python -m APySC```



`<CODE BY PYTHOFANOFF>`















