from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services import data_loader
from app.models import UploadResponse

#Define router for all upload-related endpoints
router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/", response_model=UploadResponse)
async def upload_csv(file: UploadFile = File(...)):
    #Validates File Extension is CSV
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Invalid file format. Must be .csv file")
   
    #Delegates file processing to data_loader
    await data_loader.load_csv(file)
    return UploadResponse(message="File Uploaded and Processed Successfully")