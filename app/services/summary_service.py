import pandas as pd
from datetime import datetime
from app.services import data_loader
from app.models import SummaryResponse
from fastapi import HTTPException

async def calculate_summary(user_id: int, start_date:str, end_date: str):
    #print("DEBUG — DATAFRAME:", DATAFRAME is None, len(DATAFRAME) if DATAFRAME is not None else 0)
    if data_loader.DATAFRAME is None:
        raise HTTPException(status_code=400, detail="No Data Uploaded Yet")
    df = data_loader.DATAFRAME[data_loader.DATAFRAME["user_id"] == user_id]

    if start_date:
        df=df[df["timestamp"] >= start_date]
    if end_date:
        df=df[df["timestamp"] <= end_date]
    
    if df.empty:
        raise HTTPException(status_code=404, detail="No Data found for given filters")
    
    return SummaryResponse(
        user_id=user_id,
        min_amount=df["transaction_amount"].min(),
        max_amount=df["transaction_amount"].max(),
        mean_amount=df["transaction_amount"].mean()
    )