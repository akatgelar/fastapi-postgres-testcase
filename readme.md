## RUN APP
# create virtual environtment
python -m venv venv

# activate venv
source venv/bin/activate

# create file .env from .env.example
cp .env.example .env

# install requirement
pip install -r requirements.txt

# run migration
alembic upgrade head

# run app
uvicorn app.main:app --reload

# open app
http://localhost:8000

# open documentation
http://localhost:8000/docs

# unit test
pytest


## FOR DEV
# add env to file requirements
pip freeze > requirements.txt

# alembic init
alembic init alembic

# create migration
alembic revision --autogenerate -m "migration message"

# run migration
alembic upgrade head