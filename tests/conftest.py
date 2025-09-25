import json
import os
import pytest
from utils.api_client import APIClient, DEFAULT_BASE_URL

# ---- Fixtures globales ----

@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL", DEFAULT_BASE_URL)

@pytest.fixture(scope="session")
def client(base_url) -> APIClient:
    return APIClient(base_url=base_url)

@pytest.fixture(scope="session")
def load_json():
    """Petit helper pour charger des fichiers JSON de /data ou /schemas."""
    def _loader(*path_parts):
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), *path_parts)
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return _loader

# Hook: attacher infos requête/réponse aux rapports Allure en cas d'échec
def pytest_runtest_makereport(item, call):
    # attachements Allure uniquement à l'échec de la phase 'call'
    try:
        import allure  # noqa: F401
    except Exception:
        return

    if call.when != "call":
        return

    outcome = call.excinfo
    if outcome:
        # L'utilisateur peut définir 'response' dans le test via item.funcargs
        response = item.funcargs.get("last_response", None)
        if response is not None:
            try:
                import allure
                allure.attach(
                    response.request.method + " " + response.request.url,
                    name="Request",
                    attachment_type=allure.attachment_type.TEXT,
                )
                allure.attach(
                    (response.request.body or b"").decode("utf-8") if isinstance(response.request.body, (bytes, bytearray)) else str(response.request.body or ""),
                    name="Request Body",
                    attachment_type=allure.attachment_type.JSON,
                )
                allure.attach(
                    response.text,
                    name=f"Response ({response.status_code})",
                    attachment_type=allure.attachment_type.JSON
                )
            except Exception:
                pass
