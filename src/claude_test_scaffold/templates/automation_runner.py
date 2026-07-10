from pathlib import Path
import subprocess
import sys


def run_automation(project_root: str | Path | None = None) -> int:
    root = Path(project_root or ".").resolve()
    print(f"Running automation in {root}")
    commands = [
        [sys.executable, "-m", "pytest", "-q", "api_tests"],
        [sys.executable, "-m", "pytest", "-q", "tests"],
    ]
    for command in commands:
        result = subprocess.run(command, cwd=root, capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(result.stderr)
            return result.returncode
    return 0
