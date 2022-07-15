FROM python:3.7-slim-buster

RUN mkdir -p /app

WORKDIR /app

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#copy app
COPY . .


CMD ["uvicorn", "project.main:app", "--host", "0.0.0.0", "--port", "8000"]