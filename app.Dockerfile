FROM python:3.10.4-slim

WORKDIR /recruitment-task-backend-intership-05-2022

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "main.py"]