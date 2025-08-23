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

def test_upload_valid_csv():
    csv_content = (
        "transaction_id,user_id,product_id,timestamp,transaction_amount\n"
        "1,101,501,2024-01-01 10:00:00,100.0\n"
        "2,101,502,2024-01-02 12:00:00,200.0\n"
    )
    response = client.post(
        "/upload/",
        files={"file":("test.csv",io.BytesIO(csv_content.encode()),"text/csv")},
    )
    assert response.status_code == 200
    assert response.json()["message"] == "File Uploaded and Processed Successfully"
    