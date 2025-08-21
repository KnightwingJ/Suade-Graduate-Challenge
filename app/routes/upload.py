from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services import data_loader
from app.models import UploadResponse

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/", response_model=UploadResponse)
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Invalid file format. Must be .csv file")

    await data_loader.load_csv(file)
    return UploadResponse(message="File Uploaded and Processed Successfully")