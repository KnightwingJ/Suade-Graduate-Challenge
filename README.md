# Suade-Graduate-Challenge
Graduate Challenge. Take in large dataset and return summary statistics

# Project Structure
app/
    main.py --- FastAPI entry point
    config.py --- Configs
    models.py --- Pydantic Models
    services/
        data_loader.py --- CSV Upload and Storage Logic
        summary_services.py --- Summary Calculation Logic
    routes/
        upload.py --- /upload Endpoint
        summary.py --- /summary/user_id Endpoint
    utils.py --- Helpers
        _init_.py

tests/

requirements.txt
README.md
