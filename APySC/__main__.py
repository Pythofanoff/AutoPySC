try: 
    import os, time, venv 
    from APySC.PATHS import * #PATH_FLD, PATH_FLE, REPLACE_EXISTS_FOLDERS, REPLACE_EXISTS_FILE, CNST_TXT

except ImportError as e: 
    print(f"Not enough trace dependencies: {e}")
   
 
if __name__ == "__main__":
    skipped = 0
    created = 0
    modified = 0

    sep = '-' * 15 

    start = time.time() 

    def enum_paths(target: tuple):
        global skipped, created, modified, start

        for path in target:
            if path in PATH_FLD:
                # Создание папок
                if os.path.exists(path):
                    if REPLACE_EXISTS_FOLDERS:
                        os.makedirs(path, exist_ok=True)
                        print(f'[Spent: {round(time.time() - start, 3)}]: Create {path} <- EDIT')
                        modified += 1
                    elif os.path.exists(path): 
                        # Папка уже существует
                        print(f"[Spent: {round(time.time() - start, 3)}]: The following files already exist: Create {path} <- SKIP")
                        skipped += 1
                else: 
                    os.makedirs(path, exist_ok=True)
                    print(f'[Spent: {round(time.time() - start, 3)}]: Create {path}')  
                    created += 1
            else: 
                # Создание файлов
                if os.path.exists(path):
                    if REPLACE_EXISTS_FILE: 
                        if path != '.gitignore':
                            open(path, "w", encoding="UTF-8").write('')
                            print(f'[Spent: {round(time.time() - start, 3)}]: Create {path} <- EDIT')
                            modified += 1
                        elif os.path.exists('./venv'):
                            open('.gitignore', "w", encoding="UTF-8").write(CNST_TXT)
                            print(f'[Spent: {round(time.time() - start, 3)}]: Create {path} <- EDIT')
                            modified += 1
                        elif not os.path.exists('./venv'): 
                            open('.gitignore', "w", encoding="UTF-8").write('')
                            print(f'[Spent: {round(time.time() - start, 3)}]: Create {path} <- EDIT')
                            modified += 1
                    else:
                        # Файл уже существует
                        print(f"[Spent: {round(time.time() - start, 3)}]: The following files already exist: Create {path} <- SKIP")
                        skipped += 1
                else:
                    open(path, "w", encoding="UTF-8").write('')
                    print(f'[Spent: {round(time.time() - start, 3)}]: Create {path}')
                    created += 1
 
    print('''
    ░█████╗░██████╗░██╗░░░██╗░██████╗░█████╗░ 
    ██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗ 
    ███████║██████╔╝░╚████╔╝░╚█████╗░██║░░╚═╝ 
    ██╔══██║██╔═══╝░░░╚██╔╝░░░╚═══██╗██║░░██╗ 
    ██║░░██║██║░░░░░░░░██║░░░██████╔╝╚█████╔╝ 
    ╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚═════╝░░╚════╝░ 
    
    ░██████╗████████╗░█████╗░██████╗░████████╗░░░░░░░░░ 
    ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝░░░░░░░░░ 
    ╚█████╗░░░░██║░░░███████║██████╔╝░░░██║░░░░░░░░░░░░ 
    ░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░░██║░░░░░░░░░░░░ 
    ██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░██╗██╗██╗ 
    ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝╚═╝
    ''') 

    try:
        if VENV.lower().startswith('pyvenv'):
            venv.create('venv') 
        else:
            print(f"Unknown virtual enviroment: {VENV}")

    except: print("There is no following dependency: venv") 
    
    enum_paths(PATH_FLD)
    enum_paths(PATH_FLE)

    print(''' 
    ░█████╗░██████╗░██╗░░░██╗░██████╗░█████╗░ 
    ██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗ 
    ███████║██████╔╝░╚████╔╝░╚█████╗░██║░░╚═╝ 
    ██╔══██║██╔═══╝░░░╚██╔╝░░░╚═══██╗██║░░██╗ 
    ██║░░██║██║░░░░░░░░██║░░░██████╔╝╚█████╔╝ 
    ╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚═════╝░░╚════╝░ 
    
    ███████╗██╗███╗░░██╗██╗░██████╗██╗░░██╗██╗ 
    ██╔════╝██║████╗░██║██║██╔════╝██║░░██║██║ 
    █████╗░░██║██╔██╗██║██║╚█████╗░███████║██║ 
    ██╔══╝░░██║██║╚████║██║░╚═══██╗██╔══██║╚═╝ 
    ██║░░░░░██║██║░╚███║██║██████╔╝██║░░██║██╗ 
    ╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝╚═════╝░╚═╝░░╚═╝╚═╝
    ''') 

    print(f"{sep} \n[Spent {round(time.time() - start, 3)}]: AutoPy created the project structure successfully: \nSkipped: {skipped}, \nCreated: {created}, \nModified: {modified}, \n{sep}")