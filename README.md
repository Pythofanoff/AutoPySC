<img src='logo.svg' weight=600 height=600>

# <DESCRIPTION>

 **AutoPySC** or **Auto Python Structure Creator** -
 This is a **lightweight**, simple **library for creating a project tree**.

 This library was originally written for my own small, private projects,
but I decided to keep it publicly available.
Perhaps one day this small script will grow into something bigger.

>[!Warning]
>**This library is still in the testing stage, problems are possible, please write about any errors in github issues** [Click](https://github.com/Pythofanoff/AutoPySC/issues)

## **Creates the following structure (.py, "full")**

``` txt
MyProject
├───.git
├───cache
├───docs
├───logs
├───src
│   └───my_project
│       ├───database
│       ├───images
│       ├───products
│       ├───users
│       └───utils
├───tests
└───venv
    ├───Include
    ├───Lib
    │   └───site-packages
    └───Scripts
```

### <HOW TO LAUNCH?>

1) **In terminal**: `pip install apysc` or Folder APySC, transport along the path: `\python\python38-32\lib`.
2) **In terminal**: `cd MyProject`;
3) **Configure file** `PATH.PY` under the project: `apysc open`;
4) **In terminal**: `apysc build` or `python -m apysc`.

### <OTHER COMMANDS?>

`apysc version` - Show actual version for library; <br>
`apysc clear-cache-project` - Clean up caches; <br>
`apysc` - CLI-tool.

**More information**: [Here](https://github.com/Pythofanoff/AutoPySC/blob/master/docs%2Fgetting-started.md)

**`<CODE BY PYTHOFANOFF>`**
