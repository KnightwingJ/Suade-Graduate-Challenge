# Suade-Graduate-Challenge
This is a RESTful API built with FASTAPI with the purpose of processing e-commerce transaction data and returns summary statistics, including the min, max, and mean trasaction amounts, for a specified user. This system also includes optional date filtering.<br>
This project is designed to handle large datasets, over 1M rows, and demonstrates clean code, testing and documentation best practices.

## Features
<ul>
    <li>Upload Transactions via CSV (/upload)</li>
    <li>Receive User Statistics with optional start date and end date filters (/summary/{user_id})</li>
    <li>Handles large datesets using Pandas</li>
    <li>Includes Unit Tests using pytest</li>
</ul>

## Project Structure
app/<br>
&nbsp;&nbsp;&nbsp;&nbsp;main.py --- FastAPI entry point<br>
&nbsp;&nbsp;&nbsp;&nbsp;models.py --- Pydantic Models<br>
&nbsp;&nbsp;&nbsp;&nbsp;services/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data_loader.py --- CSV Upload and Storage Logic<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary_services.py --- Summary Calculation Logic<br>
&nbsp;&nbsp;&nbsp;&nbsp;routes/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;upload.py --- /upload Endpoint<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary.py --- /summary/user_id Endpoint<br>
&nbsp;&nbsp;&nbsp;&nbsp;tests/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;test_upload.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;test_summary.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;test_large_data.py<br>
requirements.txt<br>
README.md

## Installation and Setup
<ol>
    <li>Clone the Repository
    <ul><li>git clone https://github.com/KnightwingJ/Suade-Graduate-Challenge.git</li></ul></li>
    <li>Install Dependencies
    <ul><li>pip install -r requirements.txt</li></ul></li>
    <li>Run the API
    <ul><li>uvicorn app.main:app --reload</li></ul></li>
    <li>Open in Browser
    <ul><li>API DOCS: http://127.0.0.1:8000/docs</li></ul></li>
</ol>

## API Endpoints

### 1. **Upload Transactions**
**POST /upload/**

- Uploads a CSV file with fields:
  ```
  transaction_id, user_id, product_id, timestamp, transaction_amount
  ```

Example with curl:
```bash
curl -X POST "http://127.0.0.1:8000/upload/"   -F "file=@dummy_transactions.csv"
```

Response:
```json
{
  "message": "File uploaded and processed successfully."
}
```
### 2. **Get Summary Statistics**
**GET /summary/{user_id}**

- Returns min, max, and mean transaction_amount for a given user_id.  
- Optional filters: start_date, end_date (YYYY-MM-DD or ISO datetime).

Example:
```bash
curl "http://127.0.0.1:8000/summary/101?start_date=2024-01-01&end_date=2024-02-01"
```

Response:
```json
{
  "user_id": 101,
  "min_amount": 50.0,
  "max_amount": 200.0,
  "mean_amount": 125.0
}
```
## Testing
<ul>
    <li>Run the full test suite
        <ul><li>pytest -v -s</li></ul>
    </li>
    <li>Run specific file
        <ul><li>pytest tests/test_summary.py -v</li></ul>
    </li>
</ul>

Testing includes
<ul>
    <li>Valid and invalid file uploads</li>
    <li>Summaries for users</li>
    <li>Date Filtering</li>
    <li>Large datasets</li>
</ul>

### Author
John Hinch - Suade Graduate Challenge
