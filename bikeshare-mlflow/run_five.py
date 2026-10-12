"""Ejecuta una comparación de cinco profundidades con configuración fija."""

import subprocess
import sys
from pathlib import Path


SCRIPT = Path(__file__).resolve().parent / "run_experiment.py"


def main() -> None:
    for depth in (4, 8, 12, 20, 30):
        command = [
            sys.executable,
            str(SCRIPT),
            "--n-estimators",
            "120",
            "--max-depth",
            str(depth),
            "--min-samples-leaf",
            "1",
            "--max-features",
            "1.0",
            "--random-state",
            "42",
        ]
        print(f"Ejecutando max_depth={depth}", flush=True)
        subprocess.run(command, check=True)


if __name__ == "__main__":
    main()
