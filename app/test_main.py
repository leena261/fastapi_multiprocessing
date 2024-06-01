from fastapi.testclient import TestClient
from utils.utils import get_cur_time

from .main import app

client = TestClient(app)


def test_add_process():
    response = client.post("/add_process/" , json = {
        "batchid": "batch_001",
        "payload": [[3,3],[8,8,8]]
    })
    #print(response)
    assert response.status_code == 200
    assert response.json() == {
        "batchid": "batch_001",
        "response": [6,24],
        "status": "complete", 
        "started_at": f"{get_cur_time()}", 
        "completed_at": f"{get_cur_time()}"
        }