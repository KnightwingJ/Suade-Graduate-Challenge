import pytest
from fastapi.testclient import TestClient
from app.main import app
import pandas as pd
import io

client = TestClient(app)

def generate_large_csv(num_rows=10000,  user_id=999):
    df = pd.DataFrame({
        "transaction_id":range(1,num_rows+1),
        "user_id":[user_id]*num_rows,
        "product_id":range(100,100+num_rows),
        "timestamp":pd.date_range("2024-01-01",periods=num_rows,freq="T"),
        "transaction_amount":[i % 500+1 for i in range(num_rows)]
    })
    return df.to_csv(index=False)

def test_large_dataset():
    csv_content = generate_large_csv(10000)
    response = client.post(
        "/upload/",
        files={"file":("large.csv",io.BytesIO(csv_content.encode()),"text/csv")},
    )
    assert response.status_code==200