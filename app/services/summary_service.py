import pandas as pd
from datetime import datetime
from app.services.data_loader import DATAFRAME
from app.models import SummaryResponse
from fastapi import HTTPException

async def calcualte_summary(user_id: int, start_date:str, end_date: str):
    if DATAFRAME is None:
        raise HTTPException(status_code=400, detail="No Data Uploaded Yet")
    df = DATAFRAME[DATAFRAME["user_id"] == user_id]

    if start_date:
        df=df[df["timestamp"] >= pd.to_datetime(start_date)]
    if end_date:
        df=df[df["timestamp"] <= pd.to_datetime(end_date)]
    
    if df.empty:
        raise HTTPException(status_code=404, detail="No Data found for given filters")
    
    return SummaryResponse(
        user_id=user_id,
        min_amount=df["transaction_amount"].min(),
        max_amount=df["transaction_amount"].max(),
        mean_amount=df["transaction_amount"].mean()
    )