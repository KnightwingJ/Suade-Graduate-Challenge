import pytest
from fastapi.testclient import TestClient
from app.main import app
import io

client = TestClient(app)

def test_upload_invalid_format():
    response = client.post(
        "/upload/",
        files={"file":("test.txt",io.BytesIO(b"some text"),"text/plain")},
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid file format. Must be .csv file"