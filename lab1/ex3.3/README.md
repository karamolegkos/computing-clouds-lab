# Container για τον Καιρό της Αθήνας (C)

Αυτό το πρόγραμμα (σε C με `libcurl`) καλεί το **OpenWeather API** κάθε 60 δευτερόλεπτα και εμφανίζει τα δεδομένα του καιρού για την Αθήνα.

Θα δούμε πώς το "τυλίγουμε" σε Docker με multi-stage build ώστε το τελικό image να είναι ελαφρύ και ασφαλές.

Σε αυτό το παράδειγμα το API Key δίνεται μόνο μέσω Env Var, και δεν είναι hard coded.

## Βήματα Εκτέλεσης
```shell
# Δημιουργία image
docker build -t weather-requester-c .

# Εκκίνηση container (ΠΡΟΣΟΧΗ: απαιτείται API_KEY)
docker run --name weather-c -d ^
  -e API_KEY=dcff3a1b197264b4ba1fb5fe20a6ca4b ^
  -e CITY=Athens -e STATE=Attiki -e COUNTRY=gr ^
  weather-requester-c

# Προβολή logs
docker logs -f weather-c
```

Πλέον μπορούμε να αλλάζουμε περιοχή χωρίς νέο build!
```shell
docker run --name weather-thess -d ^
  -e API_KEY=dcff3a1b197264b4ba1fb5fe20a6ca4b ^
  -e CITY=Thessaloniki -e STATE=Central-Macedonia -e COUNTRY=gr ^
  weather-requester-c
```

# **✅ Συμπεράσματα**
Με αυτό το παράδειγμα είδαμε πώς:
- Τα Environment Variables μπορούν να κάουν τον κώδικά μας πολύ δυναμικό. Δεν χρειάζεται να κάνουμε συνεχώς rebuild αν τις χρησιμοποιούμε σωστά.