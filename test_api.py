import json

from app import app

def test_tasks():
    client = app.test_client()

    # List is empty
    response = client.get('/tasks')
    assert 200 == response.status_code
    assert [] == response.json

    # Can add to list
    payload = json.dumps({"msg": "test-0"})
    response = client.post('/tasks', headers={"Content-Type": "application/json"}, data=payload)
    assert 200 == response.status_code
    assert {"id": 0, "msg": "test-0"} == response.json

    payload = json.dumps({"msg": "test-1"})
    response = client.post('/tasks', headers={"Content-Type": "application/json"}, data=payload)
    assert 200 == response.status_code
    assert {"id": 1, "msg": "test-1"} == response.json

    response = client.get('/tasks')
    assert 200 == response.status_code
    assert [{"id": 0, "msg": "test-0"}, {"id": 1, "msg": "test-1"}] == response.json

    # Can get a task
    response = client.get('/tasks/1')
    assert 200 == response.status_code
    assert {"id": 1, "msg": "test-1"} == response.json

    # Can modify list
    payload = json.dumps({"id": 1, "msg": "test-1 updated"})
    response = client.put('/tasks/1', headers={"Content-Type": "application/json"}, data=payload)
    assert 200 == response.status_code
    assert "OK" == response.data.decode("utf-8")

    response = client.get('/tasks/1')
    assert 200 == response.status_code
    assert {"id": 1, "msg": "test-1 updated"} == response.json

    # Can delete from list
    response = client.delete('/tasks/0')
    assert 200 == response.status_code
    assert {"id": 0, "msg": "test-0"} == response.json

    response = client.get('/tasks')
    assert 200 == response.status_code
    assert [{"id": 1, "msg": "test-1 updated"}] == response.json
