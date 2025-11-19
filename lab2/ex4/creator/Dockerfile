FROM python:3.11

WORKDIR /app

RUN pip install mysql-connector-python

COPY creator.py .

CMD ["python", "-u", "creator.py"]