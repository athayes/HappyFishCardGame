Install Flask: 
1. https://flask.palletsprojects.com/en/1.1.x/installation/#create-an-environment
2. https://flask.palletsprojects.com/en/1.1.x/quickstart/

Install dependencies:
pip install -r requirements.txt

Update the requirements.txt run
pip freeze > requirements.txt

To run app
* source venv/bin/activate
* python -m flask run

To run tests
python -m pytest
python -m pytest --cov=src --cov-report html