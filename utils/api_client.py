import os
import json
import requests
from typing import Any, Dict, Optional

DEFAULT_BASE_URL = "https://jsonplaceholder.typicode.com"

class APIClient:
    def __init__(self, base_url: Optional[str] = None, default_headers: Optional[Dict[str, str]] = None, timeout: int = 30):
        self.base_url = (base_url or os.getenv("BASE_URL") or DEFAULT_BASE_URL).rstrip("/")
        self.session = requests.Session()
        self.session.headers.update(default_headers or {"Content-Type": "application/json"})
        self.timeout = timeout

    def _url(self, endpoint: str) -> str:
        endpoint = endpoint if endpoint.startswith("/") else f"/{endpoint}"
        return f"{self.base_url}{endpoint}"

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None):
        return self.session.get(self._url(endpoint), params=params, timeout=self.timeout)

    def post(self, endpoint: str, payload: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        return self.session.post(self._url(endpoint), data=json.dumps(payload), headers=headers, timeout=self.timeout)

    def put(self, endpoint: str, payload: Dict[str, Any]):
        return self.session.put(self._url(endpoint), data=json.dumps(payload), timeout=self.timeout)

    def delete(self, endpoint: str):
        return self.session.delete(self._url(endpoint), timeout=self.timeout)
