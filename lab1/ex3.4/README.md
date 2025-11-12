# Container για τον Καιρό της Αθήνας (Node.js)

Αυτό το πρόγραμμα (σε Node.js 20) καλεί το **OpenWeather API** κάθε 60″ και εκτυπώνει τα δεδομένα καιρού για την Αθήνα.
Χρησιμοποιεί το global fetch (**δεν χρειάζονται έξτρα βιβλιοθήκες**).

## Βήματα Εκτέλεσης
```shell
# Δημιουργία image
docker build -t weather-requester-node .

# Εκκίνηση container (ΑΠΑΡΑΙΤΗΤΟ: API_KEY)
docker run --name weather-node -d ^
  -e API_KEY=dcff3a1b197264b4ba1fb5fe20a6ca4b ^
  -e CITY=Athens -e STATE=Attiki -e COUNTRY=gr ^
  weather-requester-node

# Προβολή logs
docker logs -f weather-node
```
Ομοίως μπορούν να αλάξουν τα Environment Variables ώστε να μην κάνουμε ξανά rebuild με την άσκηση της C.

# **✅ Συμπεράσματα**
Με αυτό το παράδειγμα είδαμε πώς:
- Ανάλογα την γλώσσα που χρησιμοποιούμε, το Dockerfile μπορεί να έχει έτοιμους χρήστες για να χρησιμοποιήσουμε αλλά και να μην υπάρχει η ανάγκη να εγκαταστήσουμε εντός της εικόνας επιπλέον βιβλιοθήκες.

