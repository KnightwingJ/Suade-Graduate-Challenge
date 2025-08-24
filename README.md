# Suade-Graduate-Challenge
This is a RESTful API built with FastAPI with the purpose of processing e-commerce transaction data and returns summary statistics, including the min, max, and mean trasaction amounts, for a specified user. This system also includes optional date filtering.<br>
This project is designed to handle large datasets, over 1M rows, and demonstrates clean code, testing and documentation best practices.

## Approach
I began this project by first reading through the requirements several times to ensure I understand what was needed. After this I began researching FastAPI as I had very little experience using it. This led to me looking into other apis and systems I might need or want, such uvicorn and Pydantic models.<br>
Knowing that I would be working with datasets I looked over my previous work using Pandas because I know it is efficient for handling large datasets.<br>
Once I had familiarized myself with the technology I would be using, I began working on the app itself, starting with the main app to create the instance of the API. Knowing that I wanted to use Pydantic models I created the models file following the basic guidlines available online. <br>
Once these models were created I made a file for loading the csv file itself using Pandas to read and parse the data into a global dataframe that could be used by other functions. After this I created the file to summarise the data based on the specified user, using the data loader function. This class also allows filtering the data by date. Once the data has been loaded, the class will return the relevant information.<br>
Knowing the required end points, I simply creating the routes for summary and upload based on the FastAPI guidlines.<br><br>
Once the application was complete, to a point, I began creating test files following the standard pytest protocols. I wanted to test that the upload functionality worked, the data would be summarised correctly, and that the API could handle large datasets.<br>
Testing the upload system was relatively simple using assert statements and dummy data to ensure that it was returning the correct statements and status codes based on RESTful practices. The summary system was giving me issues however. The system was not reading my dummy data initially which meant I was getting the wrong status code. After using looking online and using print statements to see what was inside the Dataframe, I realised that I was initially importing the global dataframe from the dataloader which was being initilised as None. Once I fixed this error, everything ran smoothly. The last thing I needed to test was could the system handle large amounts of data, but this was simple enough, it just involved creating a small function to create the dummy data and then reuse the same test functions I had used before.<br><br>
Overall, while I there is definelty room to improve with this API, I feel happy with its functionality. If it was a real system though I would be changing certain approaches, mainly instead of storing data in memory I would use a database if possible which would then entail further testing and monitoring. But for this, I think using memory is fine.

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

Uploads a CSV file with fields:
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
