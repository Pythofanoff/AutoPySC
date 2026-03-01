from importlib.metadata import version, PackageNotFoundError
import click

def get_version():
    try:
        return version('apysc')
    except PackageNotFoundError:
        return '0.0.3'

@click.group()
def cli():
    pass 

@cli.command()
def start():    
    import runpy
    
    runpy.run_module("apysc", run_name="__main__", alter_sys=True)

@cli.command(name='version', help='Show actual version of library: apysc version')
def version_cmd():
    click.echo(get_version())

@cli.command(name='open', help='Open file config: apysc open')
@click.option('-cfg', '--cfg', 'cfg_path', default='paths.py')
def open_cfg(cfg_path):
    import os, sys, importlib
    from pathlib import Path
    
    try:
        pkg = importlib.import_module("apysc")
        base_dir = Path(pkg.__file__).parent
    except Exception:
        base_dir = Path(__file__).parent  # fallback

    p = Path(cfg_path).expanduser()

    if not p.is_absolute():
        p = (base_dir / p)

    # получить абсолютный путь, не кидая ошибку, если файла нет
    p = p.resolve(strict=False)

    if not p.exists() or not p.is_file():
        click.echo(f"Файл не найден: {p}", err=True)
        raise SystemExit(1)

    try:
        if sys.platform.startswith("win"):
            os.startfile(str(p))
    except Exception as e:
        click.echo(f"Не удалось открыть {p}: {e}", err=True)
        raise

