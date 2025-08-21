import pandas as pd
from fastapi import UploadFile
from io import StringIO

#Store uploaded data in-memeory for now
DATAFRAME = None

async def load_csv(file: UploadFile):
    global DATAFRAME
    content = await file.read()
    df = pd.read_csv(StringIO(content.decode("utf-8")))
    DATAFRAME = df