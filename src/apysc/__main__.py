try: 
    import os, time, venv 
    from .paths import * # PATHS_FOLDERS, PATHS_FILES, REPLACE_EXISTS_FOLDERS, REPLACE_EXISTS_FILE, GITIGNORE
    from pathlib import Path

except ImportError as e: 
    print(f"Not enough trace dependencies: {e}")
   
def enum_paths(target: tuple):
    global skipped, created, modified, start

    for path in target:
        if path in PATHS_FOLDERS:
            # Создание папок
            if os.path.exists(path):
                if REPLACE_EXISTS_FOLDERS:
                    os.makedirs(path, exist_ok=True)
                    if not QUIET_LAUNCH:
                        print(f'[Spent: {round(time.time() - start, 3)}]: Create {path} <- EDIT')
                    modified += 1
                elif os.path.exists(path): 
                    # Папка уже существует
                    if not QUIET_LAUNCH:
                        print(f"[Spent: {round(time.time() - start, 3)}]: The following files already exist: Create {path} <- SKIP")
                    skipped += 1
            else: 
                os.makedirs(path, exist_ok=True)
                if not QUIET_LAUNCH:
                    print(f'[Spent: {round(time.time() - start, 3)}]: Create {path}')  
                created += 1
        else: 
            # Создание файлов
            if os.path.exists(path) and not REPLACE_EXISTS_FILE:
                # Файл уже существует
                if not QUIET_LAUNCH:
                    print(f"[Spent: {round(time.time() - start, 3)}]: The following files already exist: Create {path} <- SKIP")

                skipped += 1
    
            else:
                if path == '.gitignore':
                    Path(path).write_text(GITIGNORE, encoding='utf-8')

                elif path == 'LICENSE':
                    if LICENSE != '':
                        if LICENSE.lower() == 'mit':
                            Path(path).write_text(MIT, encoding='utf-8')

                    else: Path(path).write_text('', encoding='utf-8')
                
                elif path == 'README.md':
                    if DESCRIPTION != '':
                        open(path, "w", encoding="utf-8").write(DESCRIPTION) 
                            
                    else: Path(path).write_text('', encoding='utf-8')

                else:
                    import toml
                
                    Path(path).write_text('', encoding='utf-8')
                    
                    try:
                        s = toml.dumps(TOML)
                        Path("pyproject.toml").write_text(s, encoding="utf-8")
                        print(f'[Spent: {round(time.time() - start, 3)}]: Create pyproject.toml')
                    except Exception as e:
                        print(e)
                        
                        if not QUIET_LAUNCH:
                            print(f"[Spent: {round(time.time() - start, 3)}]: The following files already exist: Create {path} <- SKIP")

                if not os.path.exists(path):
                    if not QUIET_LAUNCH:
                        print(f'[Spent: {round(time.time() - start, 3)}]: Create {path}')

                    created += 1

                if os.path.exists(path):
                    if not QUIET_LAUNCH:
                        print(f'[Spent: {round(time.time() - start, 3)}]: Create {path} <- EDIT')

                    modified += 1

def main():
    try:
        if not VENV.lower().startswith('non'):
            if VENV.lower().startswith('pyven'):
                venv.create('venv') 
            else:
                if not QUIET_LAUNCH:
                    print(f"Unknown virtual enviroment: {VENV}")
    except:
        if not QUIET_LAUNCH: 
            print("There is no following dependency: venv") 


if __name__ == "__main__":
    skipped = 0
    created = 0
    modified = 0

    sep = '-' * 15 

    start = time.time() 
    
    if not QUIET_LAUNCH:
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
    
    enum_paths(PATHS_FOLDERS)
    enum_paths(PATHS_FILES)
    
    main() 

    if not QUIET_LAUNCH:
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