FROM python:3.12-slim

# Set an env var so output appears immediately
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy your script into the image
COPY python.py .

CMD ["python", "python.py"]