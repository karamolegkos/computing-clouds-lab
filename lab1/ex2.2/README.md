# Εγκατάσταση και χρήση της MongoDB

## Εγκατάσταση
Για να κατεβάσετε και να εκκινήσετε μια MongoDB instance εκτελέστε:
```shell
docker run --name my-mongo -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=1234 -p 27017:27017 -d mongo:latest
```

Στην παραπάνω εντολή χρησιμοποιούνται τα εξής:
- `--name my-mongo`: Το όνομα του container (μπορείτε να το αλλάξετε).
- `-e MONGO_INITDB_ROOT_USERNAME=admin`: Μεταβλητή περιβάλλοντος που ορίζει το όνομα χρήστη του διαχειριστή (root user).
- `-e MONGO_INITDB_ROOT_PASSWORD=1234`: Μεταβλητή περιβάλλοντος που ορίζει τον κωδικό πρόσβασης του διαχειριστή (αλλάξτε το σε κάτι ασφαλέστερο).
- `-p 27017:27017`: Εκθέτει την πόρτα 27017 του container στην πόρτα 27017 του host. Έτσι η βάση είναι προσβάσιμη και εκτός Docker (π.χ. από MongoDB Compass ή Node.js εφαρμογή).
- `-d`: Εκτελεί το container στο παρασκήνιο (detached mode).

## Έλεγχος του Container
Δείτε τη λίστα των ενεργών containers:
```shell
docker ps
```
Μία καλή ένδειξη πως το container τρέχει είναι το `Status` να εμφανίζει `Up`.

## Σύνδεση με το Mongo Shell
Για να μπείτε στο shell της MongoDB:
```shell
docker exec -it my-mongo mongosh -u admin -p 1234
```

Αν όλα πάνε καλά, θα δείτε:
```mongodb
test>
```

Μπορείτε πλέον να εκτελέσετε εντολές όπως:
```javascript
show dbs;
use testdb;
db.createCollection("users");
db.users.insertOne({ name: "Panagiotis", age: 25 });
db.users.find();
```

## Τερματισμός & Επανεκκίνηση
Τερματισμός του container:
```shell
docker stop my-mongo
```

Επανεκκίνηση:
```shell
docker start my-mongo
```

## Απεγκατάσταση
Για να διαγράψετε το container και την εικόνα:
```shell
# Δίνοντας το `-f` σταματάμε το container αν τρέχει
docker rm -f my-mongo
```

Και μετά διαγράψτε το image:
```shell
docker rmi mongo:latest
```

## Επίμονη αποθήκευση δεδομένων (Persistence - Volumes)
Για να μην χάνονται τα δεδομένα όταν διαγράφετε το container:
```shell
# Windows
docker run --name my-mongo ^
  -e MONGO_INITDB_ROOT_USERNAME=admin ^
  -e MONGO_INITDB_ROOT_PASSWORD=1234 ^
  -p 27017:27017 ^
  -v ./mongo_data:/data/db ^
  -d mongo:latest

# Linux
docker run --name my-mongo \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=1234 \
  -p 27017:27017 \
  -v ./mongo_data:/data/db \
  -d mongo:latest
```

Τα δεδομένα θα αποθηκεύονται τοπικά στον φάκελο `./mongo_data`.

# **✅ Συμπεράσματα**
Με αυτό το setup μπορείτε:
- Να εκτελέσετε εύκολα μια MongoDB μέσω Docker.
- Να τη χρησιμοποιήσετε μέσα από το shell ή εξωτερικές εφαρμογές (π.χ. MongoDB Compass, Node.js, Python).
- Να διατηρείτε τα δεδομένα σας μόνιμα μέσω volumes.