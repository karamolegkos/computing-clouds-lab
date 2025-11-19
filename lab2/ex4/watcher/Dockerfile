FROM python:3.11

WORKDIR /app

RUN pip install mysql-connector-python

COPY watcher.py .

CMD ["python", "-u", "watcher.py"]