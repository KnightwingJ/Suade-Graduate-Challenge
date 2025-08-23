import pytest
from fastapi.testclient import TestClient
from app.main import app
import io

client = TestClient(app)

#Create Sample Data before running tests
@pytest.fixture(autouse=True, scope="module")
def setup_data():
    csv_content = (
        "transaction_id,user_id,product_id,timestamp,transaction_amount\n"
        "1,101,501,2024-01-01 10:00:00,100.0\n"
        "2,101,502,2024-01-02 12:00:00,200.0\n"
        "3,102,503,2024-01-03 14:00:00,300.0\n"
    )
    client.post(
        "/upload/",
        files={"file": ("test.csv", io.BytesIO(csv_content.encode()), "text/csv")},
    )

def test_summary_valid_user():
    response = client.get("/summary/101")
    assert response.status_code==200
    data = response.json()
    assert data["user_id"] == 101
    assert data["min_amount"] == 100.0
    assert data["max_amount"] == 200.0
    assert data["mean_amount"] == 150.0