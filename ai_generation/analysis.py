from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class TestCaseSuggestion:
    title: str
    kind: str
    assertions: List[str]


class ComponentAnalyzer:
    def analyze_component(self, component_name: str, props: Dict[str, Any] | None = None) -> TestCaseSuggestion:
        props = props or {}
        assertions = [f"renders {component_name}", f"handles props: {', '.join(props.keys())}" if props else "handles default state"]
        return TestCaseSuggestion(title=f"{component_name} renders and responds to props", kind="ui-component", assertions=assertions)


class SchemaAnalyzer:
    def analyze_schema(self, schema: Dict[str, Any]) -> TestCaseSuggestion:
        required_fields = [key for key, value in schema.get("properties", {}).items() if value.get("required")]
        return TestCaseSuggestion(
            title="API response schema is validated",
            kind="api-contract",
            assertions=[f"contains required fields: {', '.join(required_fields)}" if required_fields else "contains expected payload"],
        )
