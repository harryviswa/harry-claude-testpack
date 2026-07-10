from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]


def create_template(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(content).strip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    create_template(
        ROOT / "templates" / "ui_component_test_template.md",
        """
        # UI Component Test Template
        - Target component:
        - User action:
        - Expected visible state:
        - Accessibility assertions:
        """,
    )
    create_template(
        ROOT / "templates" / "api_contract_test_template.md",
        """
        # API Contract Test Template
        - Endpoint:
        - Method:
        - Expected status:
        - Expected schema:
        - Required assertions:
        """,
    )
    print("Generated example templates in templates/.")
