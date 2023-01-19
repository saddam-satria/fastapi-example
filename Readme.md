alembic revision --autogenerate -m "init migration"
alembic upgrade head
pip freeze > requirements.txt