# Εγκατάσταση και χρήση της MinIO

## Εγκατάσταση
Για να κατεβάσετε και να εκκινήσετε ένα MinIO server container εκτελέστε:
```shell
# Windows
docker run --name my-minio ^
  -e MINIO_ROOT_USER=admin ^
  -e MINIO_ROOT_PASSWORD=12345678 ^
  -p 9000:9000 ^
  -p 9001:9001 ^
  -v ./minio_data:/data ^
  -d quay.io/minio/minio server /data --console-address ":9001"

# Linux
docker run --name my-minio \
  -e MINIO_ROOT_USER=admin \
  -e MINIO_ROOT_PASSWORD=12345678 \
  -p 9000:9000 \
  -p 9001:9001 \
  -v ./minio_data:/data \
  -d quay.io/minio/minio server /data --console-address ":9001"
```

Στην παραπάνω εντολή χρησιμοποιούνται τα εξής:
- `--name my-minio`: Το όνομα του container (μπορείτε να το αλλάξετε).
- `-e MINIO_ROOT_USER=admin`: Ορίζει το username του διαχειριστή.
- `-e MINIO_ROOT_PASSWORD=12345678`: Ορίζει τον κωδικό πρόσβασης του διαχειριστή (πρέπει να έχει τουλάχιστον 8 χαρακτήρες).
- `-p 9000:9000`: Εκθέτει το API port (για προγράμματα ή SDKs).
- `-p 9001:9001`: Εκθέτει το Web Console (UI) της MinIO.
- `-v ./minio_data:/data`: Ορίζει τοπικό φάκελο για αποθήκευση των δεδομένων (persistent storage).
- `-d`: Εκτελεί το container στο παρασκήνιο.
- `quay.io/minio/minio server /data --console-address ":9001"`: Εκκινεί τον MinIO server και το περιβάλλον διαχείρισης.

## Έλεγχος του Container
Δείτε τη λίστα των ενεργών containers:
```shell
docker ps
```
Μία καλή ένδιξη που δείχνει πως το container τρέχει, είναι το να εμφανίσει ως `Status` το `Up`.

## Πρόσβαση στο Web UI (MinIO Console)
Ανοίξτε τον browser σας και επισκεφθείτε τη διεύθυνση:
- http://localhost:9001

Θα δείτε τη σελίδα σύνδεσης του MinIO Console:
- Username: `admin`
- Password: `12345678`

Αφού συνδεθείτε, θα μπορείτε να:
- Δημιουργείτε buckets (όπως οι φάκελοι του S3)
- Ανεβάζετε/κατεβάζετε αρχεία
- Ορίζετε Access Policies για αντικείμενα ή χρήστες
- Παρακολουθείτε τη χρήση και τα logs

## Τερματισμός & Επανεκκίνηση
Τερματισμός του container:
```shell
docker stop my-minio
```

Επανεκκίνηση:
```shell
docker start my-minio
```

## Απεγκατάσταση
Για να διαγράψετε το container και την εικόνα:
```shell
# Δίνοντας το `-f` σταματάμε το container αν τρέχει
docker rm -f my-minio
```

Και μετά διαγράψτε το image:
```shell
docker rmi quay.io/minio/minio
```

# **✅ Συμπεράσματα**
Με αυτό το setup μπορείτε:
- Να εκτελέσετε εύκολα έναν MinIO server μέσω Docker.
- Να αποκτήσετε πρόσβαση στο Web UI (http://localhost:9001) για πλήρη διαχείριση.
- Να συνδέεστε προγραμματιστικά στο API (port 9000) με SDKs ή το **mc client**.
- Να διατηρείτε τα δεδομένα σας μόνιμα μέσω volumes.

