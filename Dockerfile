FROM python:3-alpine3.9

WORKDIR /fastapi

COPY requirements.txt ./

RUN dnf install -y python-pip \
    && dnf clean all \
    && pip install fastapi uvicorn aiofiles
#RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . ./

CMD ["uvicorn", "main:app", "--reload"]
