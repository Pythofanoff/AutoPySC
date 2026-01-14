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
├───logs
├───src
│   └───MyProject
│       └───database
│            └───__init__
│            └───connection
│       └───images
│       └───products
│            └───__init__
│            └───models
│            └───services
│       └───users
│            └───__init__
│            └───api
│            └───models
│            └───services
│       └───utils
│            └───__init__
│            └───helpers
├───tests
│   └───__init__
│   └───test_products
│   └───test_users
└───venv
```
Time of the structure creation: ~±500 ms

`<HOW TO LAUNCH?>`
 1) In terminal: ```pip install APySC```
 
 or:

 Folder APySC, transport along the path:     ```.\python\python38-32\lib\site-packages```
 
 2) In terminal: ```cd MyProject```
 
 3) In terminal: ```python -m APySC```



`<CODE BY PYTHOFANOFF>`














