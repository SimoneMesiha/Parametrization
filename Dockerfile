FROM python:3.8-alpine

WORKDIR /app

COPY . /app

RUN python -m pip install --upgrade pip

ENTRYPOINT ["python", "cli.py"]