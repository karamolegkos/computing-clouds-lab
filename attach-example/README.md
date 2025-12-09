# Παράδειγμα της εντολής `attach`
Δομή αυτού του φακέλου:
```text
attach-example/
├─ docker-compose.yml
└─ app/
   ├─ Dockerfile
   └─ python.py
```

### Για να εκτελέσουμε το παράδεγιμα
Χρησιμοποιώντας κάποιο τερματικό, εκτελούμε τις παρακάτω εντολές:
```bash
docker compose up -d --build
docker compose attach python_app
```
Η εντολή: `docker compose up -d --build` θα ξεκινήσει όλες τις υπηρεσίες μας. Η υπηρεσία `python_app` είναι μία εφαρμογή κονσόλας και συνεπώς εκτελείται μόνο στο τερματικό.
Η εντολή `docker compose attach python_app` μας συνδέει στο τερματικό της υπηρεσίας `python_app`.

Πατώντας `Enter` εμφανίζεται το παρακάτω:
```
Welcome to the interactive Python container!
What's your name?
```
Και πλέον μπορούμε να χρησιμοποιήσουμε κανονικά την εφαρμογή.


Η εφαρμογή ανέμεναι το `Enter` εντός του [κώδικά της](./app/python.py#L2) για να μας εμφανίσει το menu της.
