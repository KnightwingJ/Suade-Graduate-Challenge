from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Response Model for successful file uploads
class UploadResponse(BaseModel):
    message: str

#Request Model for filtering summaries
class SummaryRequest(BaseModel):
    start_date: Optional[datetime]=None
    end_date: Optional[datetime]=None

#Response Model for summary statistics
class SummaryResponse(BaseModel):
    user_id: int
    min_amount: float
    max_amount: float
    mean_amount: float