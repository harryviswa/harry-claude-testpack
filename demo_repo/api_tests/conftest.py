import pytest
        import requests

        @pytest.fixture
def api_client() -> requests.Session:
            session = requests.Session()
            session.headers.update({"Accept": "application/json"})
            return session
