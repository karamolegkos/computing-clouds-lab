FROM python:3.10-slim

WORKDIR /app

RUN pip install mysql-connector-python

COPY writer.py .

CMD ["python", "-u", "writer.py"]