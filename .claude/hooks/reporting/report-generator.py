from pathlib import Path
from datetime import datetime


def generate_report(test_results: dict | None = None, output_path: str | Path | None = None) -> Path:
    results = test_results or {"passed": 0, "failed": 0, "skipped": 0}
    output = Path(output_path or "artifacts/automation-report.md")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        "# Automation Report\n\n"
        f"- Generated: {datetime.utcnow().isoformat()}\n"
        f"- Passed: {results.get('passed', 0)}\n"
        f"- Failed: {results.get('failed', 0)}\n"
        f"- Skipped: {results.get('skipped', 0)}\n",
        encoding="utf-8",
    )
    return output
