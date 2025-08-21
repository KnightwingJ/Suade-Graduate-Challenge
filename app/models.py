from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UploadResponse(BaseModel):
    message: str

class SummaryRequest(BaseModel):
    start_date: Optional[datetime]=None
    end_date: Optional[datetime]=None

class SummaryResponse(BaseModel):
    user_id: int
    min_amount: float
    max_amount: float
    mean_amount: float