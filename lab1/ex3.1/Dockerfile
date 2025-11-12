# Χρήση επίσημης Python slim εικόνας ως βάση για ελαφρύ container
FROM python:3.12-slim

# Προαιρετικό: Βασικές ρυθμίσεις Python για containers
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Προαιρετικό: εγκατάσταση πιστοποιητικών/βασικών εργαλείων
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# Δημιουργία non-root χρήστη
RUN useradd -m -u 10001 appuser

# Ορισμός του working directory
WORKDIR /app

# Εγκαθιστούμε μόνο τα απολύτως απαραίτητα packages
RUN pip install --no-cache-dir requests

# Αντιγραφή του κώδικα της εφαρμογής
COPY main.py /app/main.py

# Εκτελούμε ως μη-προνομιούχος χρήστης
USER appuser

# Εντολή εκκίνησης της εφαρμογής
CMD ["python", "/app/main.py"]