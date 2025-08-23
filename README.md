# Suade-Graduate-Challenge
Graduate Challenge. Take in large dataset and return summary statistics

# Project Structure
app/<br>
&nbsp;&nbsp;&nbsp;&nbsp;main.py --- FastAPI entry point<br>
&nbsp;&nbsp;&nbsp;&nbsp;config.py --- Configs<br>
&nbsp;&nbsp;&nbsp;&nbsp;models.py --- Pydantic Models<br>
&nbsp;&nbsp;&nbsp;&nbsp;services/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data_loader.py --- CSV Upload and Storage Logic<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary_services.py --- Summary Calculation Logic<br>
&nbsp;&nbsp;&nbsp;&nbsp;routes/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;upload.py --- /upload Endpoint<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary.py --- /summary/user_id Endpoint<br>
&nbsp;&nbsp;&nbsp;&nbsp;utils.py --- Helpers<br>
&nbsp;&nbsp;&nbsp;&nbsp;_init_.py<br>
<br>
tests/<br>
<br>
requirements.txt<br>
README.md
