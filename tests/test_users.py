import pytest
from jsonschema import validate, Draft7Validator
from utils.api_client import APIClient

@pytest.mark.smoke
def test_get_user_schema(client: APIClient, load_json):
    schema = load_json("schemas", "user_schema.json")
    r = client.get("/users/1")
    assert r.status_code == 200
    body = r.json()

    
    errors = sorted(Draft7Validator(schema).iter_errors(body), key=lambda e: e.path)
    assert not errors, f"Schema errors: {[e.message for e in errors]}"

@pytest.mark.contract
@pytest.mark.parametrize("user_case", [
    {"id": 1, "expected_username": "Bret"},
    {"id": 2, "expected_username": "Antonette"},
])
def test_get_user_data_driven(client: APIClient, user_case, request):
    r = client.get(f"/users/{user_case['id']}")
    request.node.funcargs["last_response"] = r  
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == user_case["id"]
    assert data["username"] == user_case["expected_username"]

def test_create_user_fake(client: APIClient):
    
    payload = {
        "name": "QA Automation",
        "username": "qa_auto",
        "email": "qa@example.com"
    }
    r = client.post("/users", payload)
    assert r.status_code in (201, 200)
    data = r.json()
    
    assert "id" in data

def test_update_user_fake(client: APIClient):
    payload = {"name": "Updated QA"}
    r = client.put("/users/1", payload)
    assert r.status_code in (200, 201)
    data = r.json()
    assert data.get("name") == "Updated QA"

def test_delete_user_fake(client: APIClient):
    r = client.delete("/users/1")
    assert r.status_code in (200, 204)
