from pathlib import Path
from datetime import datetime

def generate_report(test_results=None, output_path="artifacts/automation-report.md"):
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        f"# Automation Report\n\n- Generated: {datetime.utcnow().isoformat()}\n- Passed: {test_results.get('passed', 0) if test_results else 0}\n- Failed: {test_results.get('failed', 0) if test_results else 0}\n",
        encoding="utf-8",
    )
    return output
