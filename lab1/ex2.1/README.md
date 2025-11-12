# Εγκατάσταση και χρήση της MySQL

## Εγκατάσταση
Για να κατεβάσετε και να εκκινήσετε μια MySQL instance εκτελέστε:
```shell
docker run --name my-mysql -e MYSQL_ROOT_PASSWORD=1234 -p 3306:3306 -d mysql:latest
```

Στην παραπάνω εντολή χρησιμοποιούνται τα εξής:
- `--name my-mysql`: Το όνομα του container (μπορείτε να το αλλάξετε).
- `-e MYSQL_ROOT_PASSWORD=1234`: Μεταβλητή περιβάλλοντος (Environment Variable) που ορίζει τον κωδικό πρόσβασης για τον χρήστη `root` (αλλάξτε το σε κάτι ασφαλέστερο αν θέλετε).
- `-p 3306:3306`: Εκθέτει την πόρτα 3306 του container στην πόρτα 3306 του host. Αυτός επιτρέπει στο DBMS να δέχεται πρόσβαση έξω από το container.
- `-d`: Εκτελεί το container στο παρασκήνιο (detached mode).
- `mysql:latest`: Χρησιμοποιεί την τελευταία έκδοση του επίσημου MySQL image από το DockerHub.

## Έλεγχος του Container
Δείτε τη λίστα των ενεργών containers:
```shell
docker ps
```
Μία καλή ένδιξη που δείχνει πως το container τρέχει, είναι το να εμφανίσει ως `Status` το `Up`.

## Σύνδεση με το MySQL Shell
Για να μπείτε στο shell της MySQL:
```shell
docker exec -it my-mysql mysql -u root -p
# Θα σας ζητηθεί ο κωδικός (στο παράδειγμα: 1234)
```

Αν όλα πάνε καλά, θα δείτε:
```mysql
mysql>
```

Μπορείτε πλέον να εκτελέσετε τα παρακάτω:
```sql
SHOW DATABASES;
CREATE DATABASE testdb;
USE testdb;
```

## Τερματισμός & Επανεκκίνηση
Τερματισμός του container:
```shell
docker stop my-mysql
```

Επανεκκίνηση:
```
docker start my-mysql
```

## Απεγκατάσταση

Για να διαγράψεται την εικόνα, πρώτα πρέπει να σταματήσετε (`stop`) και να διαγράψετε το container:
```shell
# Δίνοντας το `-f` σταματάμε το container στην περίπτωση που τρέχει, 
# πριν το διαγράψουμε
docker rm -f my-mysql
```

Και τελικά διαγράφουμε την εικόνα:
```shell
docker rmi mysql:latest
```

## Επίμονη αποθήκευση δεδομένων (Persistence - Volumes)
Για να μην χάνονται τα δεδομένα όταν διαγράφετε το container:
```shell
# Windows
docker run --name my-mysql ^
  -e MYSQL_ROOT_PASSWORD=1234 ^
  -p 3306:3306 ^
  -v ./mysql_data:/var/lib/mysql ^
  -d mysql:latest

# Linux
docker run --name my-mysql \
  -e MYSQL_ROOT_PASSWORD=1234 \
  -p 3306:3306 \
  -v ./mysql_data:/var/lib/mysql \
  -d mysql:latest
```

Τα δεδομένα θα αποθηκεύονται τοπικά στον φάκελο `./mysql_data`.

✅ **Συμπέρασμα**: Αν εμφανίστηκε το μήνυμα **“Hello from Docker!**”, τότε η εγκατάσταση του Docker σας είναι επιτυχής και είστε έτοιμοι να δημιουργήσετε και να εκτελέσετε τα δικά σας containers!