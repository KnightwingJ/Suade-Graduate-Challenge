from fastapi import APIRouter,Query
from app.services import summary_service
from app.models import SummaryResponse
from datetime import datetime
from typing import Optional

#Define router for all summary-related endpoints
router = APIRouter(prefix="/summary",tags=["Summary"])

@router.get("/{user_id}", response_model=SummaryResponse)
async def get_summary(
    user_id: int,
    start_date: Optional[datetime]=Query(None),
    end_date: Optional[datetime] = Query(None)
):
    #Get Summary Statistics for specified user, including min,max, and mean
    return await summary_service.calculate_summary(user_id,start_date,end_date)