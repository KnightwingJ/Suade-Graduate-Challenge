from fastapi import APIRouter,Query
from app.services import summary_service
from app.models import SummaryResponse

router = APIRouter(prefix="/summary",tags=["Summary"])

@router.get("/{user_id}", response_model=SummaryResponse)
async def get_summary(user_id: int,
                      start_date: str=Query(None),
                      end_date: str = Query(None)):
    return await summary_service.calculate_summary(user_id,start_date,end_date)