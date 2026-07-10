import pytest

from api_tests.helpers.api_helpers import get_json


@pytest.mark.parametrize("resource_id", [1, 2, 3])
def test_get_todos_endpoint_returns_json(api_client, api_base_url, resource_id):
    response = get_json(api_client, f"{api_base_url}/todos/{resource_id}")
    assert isinstance(response, dict)
    assert "id" in response
    assert response["id"] == resource_id
