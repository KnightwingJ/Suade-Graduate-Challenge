from fastapi import FastAPI
from app.routes import upload,summary
# Create the FASTAPI instance
app = FastAPI(
    title = "Graduate Challenge Suade - John Hinch",
    description= "API for processing large datasets and returning summary",
    version= "1.0.0"
)
#Register API routes
app.include_router(upload.router)
app.include_router(summary.router)