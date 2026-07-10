from pathlib import Path
import subprocess
import sys

def main() -> int:
    root = Path(__file__).resolve().parents[1]
    for target in ["api_tests", "tests"]:
        result = subprocess.run([sys.executable, "-m", "pytest", "-q", target], cwd=root)
        if result.returncode != 0:
            return result.returncode
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
