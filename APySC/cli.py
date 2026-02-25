from __main__ import 
def start():
    import argparse, runpy 

    parser = argparse.ArgumentParser(prog="apysc")
    parser.add_argument("--version", action="version", version="0.1.0")
    parser.add_argument("start", nargs="?", action=main())
    args = parser.parse_args()

def main():
    runpy.run_module("mypkg", run_name="__main__", alter_sys=True)