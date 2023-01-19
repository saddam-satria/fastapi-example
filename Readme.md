pip install --no-cache-dir --upgrade -r /fastapi/requirements.txt
alembic revision --autogenerate -m "init migration"
alembic upgrade head
pip freeze > requirements.txt
