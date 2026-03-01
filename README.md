<img src='logo.svg' weight=600 height=600>

# <DESCRIPTION>
 
v. of lib: `0.0.3`

 **AutoPySC** or **Auto Python Structure Creator** - 
 This is a **lightweight**, simple **library for creating a project tree**.

 This library was originally written for my own small, private projects, 
but I decided to keep it publicly available. 
Perhaps one day this small script will grow into something bigger.

>[!Warning]
>This library is still in the testing stage, problems are possible, please write about any errors in github issues [Click](https://github.com/Pythofanoff/AutoPySC/issues)

## Creates the following structure:
```
MyProject
└───.git
└───cache
└───logs
└───venv
└───.gitignore
└───LICENCE
└───pyproject.toml
└───README.MD
├───docs
│   └───index.md
└───src
    └───tests
    │    └───__init__.py
    │    └───test_products.py
    │    └───test_users.py
    └───MyProject
        └───images
        └───database
        │    └───__init__.py
        │    └───connection.py
        └───products
        │    └───__init__.py
        │    └───models.py
        │    └───services.py
        └───users
        │    └───__init__.py
        │    └───api.py
        │    └───models.py
        │    └───services.py
        └───utils
             └───__init__.py
             └───helpers.py
```

### <HOW TO LAUNCH?>
1) In terminal: `pip install APySC` or Folder APySC, transport along the path: `.\python\python38-32\lib`
 
2) In terminal: `cd MyProject`
 
3) Configure file `PATH.PY` under the project: `apysc open` 
 
4) In terminal: `apysc start` or `python -m APySC`

#### **`<Other commands>`**
`apysc version` - Show actual version for library

`<CODE BY PYTHOFANOFF>`
































