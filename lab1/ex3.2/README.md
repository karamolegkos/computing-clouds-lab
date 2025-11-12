# Container για τον Καιρό της Αθήνας (Java)

Αυτό το πρόγραμμα καλεί το OpenWeather API κάθε 60 δευτερόλεπτα και εμφανίζει τα δεδομένα του καιρού για την Αθήνα.
Θα δούμε πώς το "τυλίγουμε" σε Docker (compile σε JDK και run σε JRE).

## Τι πρέπει να προσέχουμε όταν γράφουμε Dockerfile
Το Dockerfile είναι ο "οδηγός κατασκευής" για το container μας. Κάθε εντολή δημιουργεί layer, στόχος: ελαφρύ, ασφαλές, προβλέψιμο image.
1. Σωστή βάση (base image)
- Για build χρησιμοποιούμε JDK (`eclipse-temurin:21-jdk`), για runtime JRE (`eclipse-temurin:21-jre`).
- Αποφεύγουμε `latest`, προτιμάμε συγκεκριμένες εκδόσεις (π.χ. `21`).
2. Multi-stage build
- Κάνουμε compile σε ένα stage, και στο τελικό image κρατάμε μόνο τα απαραίτητα (class/jar).
- Μικρότερο μέγεθος, λιγότερες επιφάνειες επίθεσης.
3. WORKDIR / COPY
- WORKDIR `/app` και COPY μόνο των απαραίτητων αρχείων (π.χ. `Main.java`).
4. Μη χρήση root
- Τρέχουμε με απλό χρήστη (USER `appuser`) για ασφάλεια.
5. CMD vs ENTRYPOINT
- `CMD ["java","Main"]` είναι αρκετό εδώ. Μπορούμε να το αλλάξουμε εύκολα στο `docker run`.

## Βήματα Εκτέλεσης
```shell
# Δημιουργία image
docker build -t weather-requester-java .

# Εκκίνηση container
docker run --name weather-java -d ^
  -e API_KEY=dcff3a1b197264b4ba1fb5fe20a6ca4b ^
  weather-requester-java

# Προβολή logs
docker logs -f weather-java
```

# **✅ Συμπεράσματα**
Με αυτό το παράδειγμα είδαμε πώς:
- Γράφουμε έναν Java client με το built-in HttpClient
- Χτίζουμε image με `multi-stage Dockerfile` (JDK→JRE)
- Τρέχουμε απομονωμένα σε container και βλέπουμε logs
- Χειριζόμαστε με ασφάλεια API keys μέσω `ENV vars`