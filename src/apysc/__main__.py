import json
import os
import time
import venv
from datetime import datetime
from pathlib import Path

import toml
from colorama import Fore, Style, init

from .constants import (
    GITIGNORE,
    MIT,
    ApacheLicenseVersion2,
    TOML
) 

from .paths import (
    NAME_OF_PROJECT,
    DESCRIPTION,
    LICENSE,
    VENV,
    LANGUAGE,
    ARCHITECTURE,
    REPLACE_EXISTS_FILE,
    QUIET_LAUNCH
)

init(autoreset=True)

class Builder:
    DOT_WIDTH = 40
    def __init__(self):
        self.skipped = 0
        self.created = 0
        self.modified = 0

        current_time = datetime.now().strftime("%H:%M:%S:%m")

        config_path = Path(__file__).parent / "paths.json"
        with config_path.open(encoding="utf-8") as f:
            self.cfg = json.load(f)

        print(f"\r[ {Fore.LIGHTBLUE_EX}{current_time}{Fore.RESET} ]: Creating {Fore.LIGHTBLACK_EX}Virtual enviroments... ", end='', flush=True)
        self.builder_venv()
        print(f"[ {Fore.LIGHTBLUE_EX}{current_time}{Fore.RESET} ]: Creating {Fore.LIGHTMAGENTA_EX}folders...")
        self.builder_folders()
        print(f"[ {Fore.LIGHTBLUE_EX}{current_time}{Fore.RESET} ]: Creating {Fore.LIGHTCYAN_EX}files...")
        self.builder_files()

    def builder_folders(self):
        FOLDERS_PATHS = self.cfg[LANGUAGE][ARCHITECTURE]["folders_path"]
        
        for folder_path in FOLDERS_PATHS:
            current_time = datetime.now().strftime("%H:%M:%S:%m")
            
            folder_path = folder_path.replace("{NAME_OF_PROJECT}", NAME_OF_PROJECT)

            os.makedirs(folder_path, exist_ok=True)
            print(
                f"└───[ {Fore.LIGHTBLUE_EX}{current_time}{Fore.RESET} ]: "
                f"{Fore.LIGHTMAGENTA_EX}{folder_path + ' ':.<{self.DOT_WIDTH}} "
                f"{Fore.LIGHTGREEN_EX}CREATED"
            )
            self.created += 1

    def builder_files(self):
        FILES_PATHS = self.cfg[LANGUAGE][ARCHITECTURE]["files_path"]

        for file_path in FILES_PATHS:
            current_time = datetime.now().strftime("%H:%M:%S:%m")
            file_path = file_path.replace("{NAME_OF_PROJECT}", NAME_OF_PROJECT)

            is_file_exists = os.path.exists(file_path)

            if is_file_exists and not REPLACE_EXISTS_FILE:
                print(
                    f"└───[ {Fore.LIGHTBLUE_EX}{current_time}{Fore.RESET} ]: "
                    f"{Fore.LIGHTCYAN_EX}File{Fore.RESET} already {Fore.LIGHTRED_EX}exists{Fore.RESET}: "
                    f"{Fore.LIGHTCYAN_EX}{file_path + ' ':.<{self.DOT_WIDTH}} "
                    f"{Fore.LIGHTRED_EX}SKIPPED"
                )
                self.skipped += 1
                continue

            if file_path == ".gitignore":
                Path(file_path).write_text(GITIGNORE, encoding="utf-8")
            elif file_path == "LICENSE":
                if not LICENSE.isspace():
                    if LICENSE.lower() == "mit":
                        Path(file_path).write_text(MIT, encoding="utf-8")
                else: Path(file_path).write_text("", encoding="utf-8")
            elif file_path == "README.md":
                if not DESCRIPTION.isspace():
                    open(file_path, "w", encoding="utf-8").write(DESCRIPTION)                             
                else: Path(file_path).write_text("", encoding="utf-8")
            elif file_path == "pyproject.toml":
                Path(file_path).write_text("", encoding="utf-8")        
                try:
                    s = toml.dumps(TOML)
                    Path("pyproject.toml").write_text(s, encoding="utf-8")
                except Exception as e:
                    print(e)
                    print(
                        f"└───[ {Fore.LIGHTBLUE_EX}{current_time}{Fore.RESET} ]: "
                        f"{Fore.LIGHTCYAN_EX}File{Fore.RESET} already {Fore.LIGHTRED_EX}exists{Fore.RESET}: "
                        f"{Fore.LIGHTCYAN_EX}{file_path + ' ':.<{self.DOT_WIDTH}} "
                        f"{Fore.LIGHTRED_EX}SKIPPED"
                    ) 
            else:
                Path(file_path).write_text("", encoding="utf-8")        

            if is_file_exists and REPLACE_EXISTS_FILE:
                print(
                    f"└───[ {Fore.LIGHTBLUE_EX}{current_time}{Fore.RESET} ]: "
                    f"{Fore.LIGHTCYAN_EX}File{Fore.RESET} already {Fore.LIGHTYELLOW_EX}exists{Fore.RESET}: "
                    f"{Fore.LIGHTCYAN_EX}{file_path + ' ':.<{self.DOT_WIDTH}} " 
                    f"{Fore.LIGHTYELLOW_EX}MODIFIED"
                )
                self.modified += 1    
            elif not is_file_exists:
                print(
                    f"└───[ {Fore.LIGHTBLUE_EX}{current_time}{Fore.RESET} ]: "
                    f"{Fore.LIGHTCYAN_EX}{file_path + ' ':.<{self.DOT_WIDTH}} "
                    f"{Fore.LIGHTGREEN_EX}CREATED"
                )
                self.created += 1

    def builder_venv(self):
        if VENV.lower().startswith("pyven"):
            venv.create("venv")     
        elif VENV.lower().startswith("poetry"):
            pass 
        else:
            print(f'{Fore.LIGHTRED_EX}ERROR')
            return 
    
        print(f'{Fore.LIGHTGREEN_EX}CREATED')


if __name__ == "__main__":
    sep = "#" * 78

    start = time.time() 
    
    if not QUIET_LAUNCH:
        print(f"""{Fore.LIGHTCYAN_EX}
_________________  _________________     
___    |__  __ \ \/ /_  ___/_  ____/    
__  /| |_  /_/ /_  /_____ \_  /       
_  ___ |  ____/_  / ____/ // /___        
/_/  |_/_/     /_/  /____/ \____/
{Fore.RESET}""")
    
    builder = Builder()

    if not QUIET_LAUNCH:
        print(f"""{Fore.LIGHTCYAN_EX}
_____________________   _____________________  __
___  ____/___  _/__  | / /___  _/_  ___/__  / / /
__  /_    __  / __   |/ / __  / _____ \__  /_/ / 
_  __/   __/ /  _  /|  / __/ /  ____/ /_  __  /  
/_/      /___/  /_/ |_/  /___/  /____/ /_/ /_/   
    """) 

    spent_time = round(time.time() - start, 3)
    print(
        f"\n{sep}\n"
        f"# "
        f"{Fore.LIGHTGREEN_EX}BUILD SUCCEFULL{Fore.RESET} "
        f"in {Fore.LIGHTMAGENTA_EX}{spent_time}ms{Fore.RESET}"
        f"{' ' * (70 - len(f'{Fore.LIGHTGREEN_EX}BUILD SUCCEFULL') - 1)}#"
    )
    print(f"""
#----------------------------------------------------------------------------#
# {Fore.LIGHTGREEN_EX}{f'CREATED: {builder.created} files':<75}{Fore.RESET}#\n
# {Fore.LIGHTRED_EX}{f'SKIPPED: {builder.skipped} files':<75}{Fore.RESET}#\n
# {Fore.LIGHTYELLOW_EX}{f'MODIFIED: {builder.modified} files':<75}{Fore.RESET}#\n                                                                
##############################################################################
""")    
