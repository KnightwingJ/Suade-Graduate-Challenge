import pandas as pd
from datetime import datetime
from app.services import data_loader
from app.models import SummaryResponse
from fastapi import HTTPException

async def calculate_summary(user_id: int, start_date:str, end_date: str):
    #Ensure data has been uploaded
    if data_loader.DATAFRAME is None:
        raise HTTPException(status_code=400, detail="No Data Uploaded Yet")
    
    #Filter for this specific user
    df = data_loader.DATAFRAME[data_loader.DATAFRAME["user_id"] == user_id]

    # Apply date range filters if provided
    if start_date:
        df=df[df["timestamp"] >= start_date]
    if end_date:
        df=df[df["timestamp"] <= end_date]
    
    #No transactions found after filtering
    if df.empty:
        raise HTTPException(status_code=404, detail="No Data found for given filters")
    
    # Return summary statistics as a Pydantic response model
    return SummaryResponse(
        user_id=user_id,
        min_amount=df["transaction_amount"].min(),
        max_amount=df["transaction_amount"].max(),
        mean_amount=df["transaction_amount"].mean()
    )