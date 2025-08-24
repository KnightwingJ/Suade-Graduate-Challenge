import pandas as pd
from fastapi import UploadFile
from io import StringIO

#Store uploaded data in-memeory for now
DATAFRAME = None

async def load_csv(file: UploadFile):
    #Reads and parses CSV into Pandas DataFrame
    global DATAFRAME
    content = await file.read()
    #Parses timestamp as datetime
    df = pd.read_csv(StringIO(content.decode("utf-8")), parse_dates=["timestamp"])
    #Stores DataFrame in a global variable for later use
    DATAFRAME = df