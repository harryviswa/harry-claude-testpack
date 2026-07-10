from typing import Any, Dict

import requests


def get_json(session: requests.Session, url: str, **kwargs) -> Dict[str, Any]:
    response = session.get(url, **kwargs)
    response.raise_for_status()
    return response.json()


def post_json(session: requests.Session, url: str, payload: Dict[str, Any], **kwargs) -> Dict[str, Any]:
    response = session.post(url, json=payload, **kwargs)
    response.raise_for_status()
    return response.json()
