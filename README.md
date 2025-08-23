# Suade-Graduate-Challenge
Graduate Challenge. Take in large dataset and return summary statistics

# Project Structure
app/<br>
    main.py --- FastAPI entry point<br>
    config.py --- Configs<br>
    models.py --- Pydantic Models<br>
    services/<br>
        data_loader.py --- CSV Upload and Storage Logic<br>
        summary_services.py --- Summary Calculation Logic<br>
    routes/<br>
        upload.py --- /upload Endpoint<br>
        summary.py --- /summary/user_id Endpoint<br>
    utils.py --- Helpers<br>
        _init_.py<br>
<br>
tests/<br>
<br>
requirements.txt<br>
README.md
