FROM python:3-alpine3.9

WORKDIR /fastapi

COPY requirements.txt ./

#RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . ./

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]