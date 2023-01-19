FROM python:3-alpine3.9

WORKDIR /fastapi

COPY requirements.txt ./

#RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /fastapi/requirements.txt

COPY . /fastapi

CMD ["python", "main.py"]