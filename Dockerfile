FROM python:3.8

WORKDIR /FastBot

COPY requirements.txt /FastBot/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /FastBot/requirements.txt

COPY . /FastBot

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
