# Lab 1 - Docker & Containerization 🐳

## Δομή του Μαθήματος
- Εισαγωγή στο Docker 
- Multicontainer Applications
- Docker Images
- Docker Containers

Σε αυτόν τον φάκελο μπορείτε να βρείτε παραδείγματα κατασκευής Python3 εφαρμογών και τελικά το containerization τους.

Μπορείτε να βρείτε εξήγηση του τρόπου διαχείρισης του Docker Engine στον φάκελο [docker-management](docker-management).

## Ασκήσεις
- **[Ex1](ex1)**: Εκτέλεση του Docker **Hello World**.
- **[Ex2.1](ex2.1)**: Εγκατάσταση και χρήση της **MySQL**.
- **[Ex2.2](ex2.2)**: Εγκατάσταση και χρήση της **MongoDB**.
- **[Ex2.3](ex2.3)**: Εγκατάσταση και χρήση της **MinIO**.
- **[Ex2.4](ex2.4)**: Εγκατάσταση ενός **Jupiter Notebook**.
- **[Ex3.1](ex3.1)**: Καιρός Αθήνας μέσω **Python** (Δημιουργία Image και Container)
- **[Ex3.2](ex3.2)**: Καιρός Αθήνας μέσω **Java** (Δημιουργία Image και Container)
- **[Ex3.3](ex3.3)**: Καιρός Αθήνας μέσω **C** (Δημιουργία Image και Container)
- **[Ex3.4](ex3.4)**: Καιρός Αθήνας μέσω **Node.js** (Δημιουργία Image και Container)

## Προεραιτική Εργασία
Σκοπός της εργασίας αυτής είναι η δημιουργία ενός Docker Image.

Θα κατασκευάσετε ένα script (Σε όποια γλώσσα επιθυμείτε) το οποίο ζητάει δεδομένα καιρού για το δήμο της Αθήνας μέσω του **OpenWeatherMap API**. Μπορείτε να λάβετε βοήθεια από τις ασκήσεις που παρουσιάστηκαν στο Lab1 (**Ασκήσεις Ex3.1 - Ex3.4**).

Θα πρέπει να εμφανίζεται ο καιρός με την θερμοκρασία κάθε ένα λεπτό. Παραδειγματικά:: `Clouds | 294.13 F`.

Τα βήματα που θα πρέπει να ακολουθήσετε είναι τα παρακάτω:
- Δημιουργήστε ένα Docker Ιmage χρησιμοποιώντας το σωστό Dockerfile.
  - Χρησιμοποιήστε ως φάκελο εργασίας (WORKDIR) τον φάκελο app.
  - Αντιγράψτε τον κώδικά σας εντός του image, στον φάκελο app.
  - Εγκαταστήστε κατά την δημιουργία του image, τις απαραίτητες βιβλιοθήκες για το script σας.
  - Δημιουργήστε ένα `ENTRYPOINT` ή ένα αρχικό `COMMAND` στο script σας, με βάση την γλώσσα που χρησιμοποιήσατε.
- Χτίστε το image τοπικά (Ονομάστε το image σας `lab2`).
- Τρέξτε το image και εμφανίστε τα logs (Για να δείτε ότι λειτουργεί).
- Ανεβάστε το Image που φτιάξατε στο **[DockerHub](https://hub.docker.com/)**.

Παράδοση στον Αρίσταρχο (1η Προαιρετική Εργασία):
- Να ανεβάσετε ένα `.txt` αρχείο με το link για το DockerHub εντός ενός zip φακέλου.
- Όνομα Αρχείου: `<Αριθμός Μητρώου>.zip` (Πχ. `e17065.zip`)

## Extra Άσκηση (Εγκατάσταση ενός Minecraft Server)
Για να κατεβάσετε και να εκκινήσετε έναν Minecraft Server εκτελέστε:
```shell
docker run --name my-minecraft ^
  -d -p 25565:25565 ^
  -e EULA=TRUE ^
  -e VERSION=latest ^
  -e DIFFICULTY=normal ^
  -e MAX_PLAYERS=5 ^
  -e MOTD="Καλώς ήρθατε στον Dockerized Server!" ^
  -v ./minecraft_data:/data ^
  itzg/minecraft-server
```

### Σύνδεση στο Minecraft Server
Ανοίξτε το Minecraft και από το μενού Multiplayer, επιλέξτε Add Server.

Συμπληρώστε:
- Server Name: `My Docker Server`
- Server Address: `localhost` (ή η IP του μηχανήματος αν παίζουν άλλοι στο LAN).

Πατήστε **Join Server** και συνδεθείτε!