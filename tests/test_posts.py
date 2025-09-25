import json
import pytest
from jsonschema import Draft7Validator
from utils.api_client import APIClient

@pytest.mark.smoke
def test_get_post_schema(client: APIClient, load_json):
    schema = load_json("schemas", "post_schema.json")
    r = client.get("/posts/1")
    assert r.status_code == 200
    body = r.json()

    errors = sorted(Draft7Validator(schema).iter_errors(body), key=lambda e: e.path)
    assert not errors, f"Schema errors: {[e.message for e in errors]}"

@pytest.mark.parametrize("post_case", json.load(open("data/posts.json", encoding="utf-8")))
def test_create_post_data_driven(client: APIClient, post_case, request):
    r = client.post("/posts", post_case)
    request.node.funcargs["last_response"] = r
    assert r.status_code in (201, 200)
    body = r.json()
    # L'API renvoie le payload + un id simulé
    for k, v in post_case.items():
        assert body.get(k) == v
    assert "id" in body

def test_update_post(client: APIClient):
    payload = {"id": 1, "title": "updated title", "body": "updated body", "userId": 1}
    r = client.put("/posts/1", payload)
    assert r.status_code in (200, 201)
    body = r.json()
    assert body["title"] == "updated title"
    assert body["body"] == "updated body"

def test_delete_post(client: APIClient):
    r = client.delete("/posts/1")
    assert r.status_code in (200, 204)
