from pathlib import Path
import json


def cfg_open(path: str):
    config_path = Path(__file__).resolve().parents[2] / path 

    with config_path.open(encoding="utf-8") as f:
        cfg = json.load(f)

    return cfg