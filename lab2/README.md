# Lab 2 - Docker Compose & Multi-Service Environments 🧩

## Δομή του Μαθήματος
- Εισαγωγή στο Docker Compose
- Δομή αρχείου `docker-compose.yml`
  - Services
  - Depends On
  - Ports
  - Volumes
  - Environment Variables
- Networks & επικοινωνία μεταξύ services

Στο Lab 2 θα μάθετε πώς να δημιουργείτε multi-container εφαρμογές χρησιμοποιώντας το **Docker Compose**.

Θα μάθουμε πώς ορίζουμε πολλαπλά services, πώς αυτά επικοινωνούν μεταξύ τους, πώς αποθηκεύονται δεδομένα με volumes και πώς χρησιμοποιούμε compose commands για logs, εκκίνηση και τερματισμό.

## Ασκήσεις
- **[Ex1](ex1)**: MySQL + εφαρμογή Writer (inserts σε DB)
- **[Ex1.1](ex1.1)**: MySQL + εφαρμογή Writer (inserts σε DB) - ως daemon
- **[Ex2](ex2)**: MySQL + Writer + Adminer (web UI)
- **[Ex2.1](ex2.1)**: MySQL + Writer + Adminer (web UI) - ως daemon
- **[Ex3](ex3)**: MinIO + script upload/download + Web Console
- **[Ex4](ex4)**: MySQL + 2 Python Services

## Προεραιτική Εργασία
Στόχος: Να φτιάξετε ένα μικρό σύστημα με Docker Compose, όπου ένα δικό σας service (`writer`) τρέχει συνεχώς και:
1. Παίρνει έναν ακέραιο από environment variable (`SEED_NUMBER`).
2. Συνδυάζει το `SEED_NUMBER` με το τρέχον `timestamp`.
3. Χρησιμοποιεί έναν συγκεκριμένο hash function για να παράγει "τυχαίους" ακεραίους.
4. Γράφει δεδομένα σε MySQL.
5. Κάθε 1 λεπτό:
  - διαβάζει τα δεδομένα από τη βάση για εκείνο το iteration,
  - δημιουργεί ένα καινούριο report file σε volume.

Το `writer` τρέχει μέσα σε `while True` loop και συνεχίζει μέχρι να σταματήσετε το container.

Εντός του `docker-compose.yml` πρέπει να υπάρχουν οι παρακάτω υπηρεσίες (services):
- `mysqldbms`: Για την Βάση Δεδομένων σας. Πρέπει το `writer` να έχει πρόσβαση.
- `writer`: 
  - Χτίζεται από δικό σας Dockerfile.
  - Λαμβάνει μία Μεταβλητή Περιβάλλοντος με όνομα `SEED_NUMBER`.
  - Αφήνει αρχεία στο host machine στον φάκελο `./output`.
  - Δεν ξεκινάει αν δεν έχει ξεκινήσει η υπηρεσία `mysqldbms`.

### Hash Function
Το Hash Function που θα χρησιμοποιηθεί είναι το ακόλουθο (*σε ψευδοκώδικα*):
```
function hash(x):
    return ((x * 7919) + 11) mod 100000
```
> Το αποτέλεσμα είναι πάντα ακέραιος από `0` έως `99999`.

### Λειτουργία `writer`
Σε κάθε βρόχο του `while True` εντός του `writer` θα γίνονται τα παρακάτω:
1. Παίρνετε την τρέχουσα χρονική στιγμή (timestamp), π.χ. σε δευτερόλεπτα ή λεπτά.
2. Υπολογίζεται το `x` με την παρακάτω λογική:
> Για Δευτερόλεπτα:
```
now = current_unix_timestamp_in_seconds()
combined = SEED_NUMBER + now
x = hash(combined)
```
> Για Λεπτά:
```
now_minutes = floor(current_unix_timestamp_in_seconds() / 60)
combined = SEED_NUMBER + now_minutes
x = hash(combined)
```
> (σημασία έχει ότι σε διαφορετικό λεπτό παίρνετε διαφορετικό αρχικό x).

3. Δημιουργεί πίνακα (αν δεν υπάρχει) π.χ. `random_values`:
  - id (PRIMARY KEY, AUTO_INCREMENT)
  - value (INT)

4. Εκτελεί πρακτικά το παρακάτω query:
  - `INSERT INTO random_values(value) VALUES (x)`

5. Εκτυπώνει στα logs του container το παρακάτω:
```
Inserted value 12345
```
> Θα πρέπει αντί για `12345` να εμφανίζεται η πραγματική τιμή που γράφτηκε στην βάση.

6. Διαβάζει **ΟΛΕΣ** τις τιμές από τον πίνακα random_values.

7. Υπολογίζει τον μέσο όρο (average) όλων των τιμών που υπάρχουν στον πίνακα.

8. Γράφει ένα μικρό report αρχείο μέσα στο volume `./output`, π.χ. με όνομα αρχείου: `report_<TIMESTAMP>.txt`
  - Το αρχείο θα πρέπει να έχει μέσα την παρακάτω πληροφορία:
```
Timestamp: <τρέχοντας χρόνος>
Total values stored: <πόσες τιμές έχει η βάση>
Average value: <μέσος όρος>
```

9. Θα περιμένει 60 δευτερόλεπτα πριν συνεχίσει στην επόμενη επανάληψη.

### Εκτέλεση
Η εργασία θα πρέπει να μπορεί να εκτελεστεί ολόκληρη με την παρακάτω εντολή:
```
docker compose up -d --build
```

Με αυτό θα πρέπει να:
- χτιστεί το image του writer,
- εκκινήσει το mysqldbms,
- εκκινήσει το writer μόνο αφού είναι έτοιμη η βάση.

Για να δείτε ότι το `writer` εκτελείται σωστά και δημιουργεί αρχεία κάθε 1 λεπτό:
```
docker compose logs writer
```

Ο φάκελος `./output` στο host πρέπει να γεμίζει με αρχεία τύπου:
```
report_20250119_1403.txt
report_20250119_1404.txt
report_20250119_1405.txt
```

Η εργασία θα πρέπει να μπορεί να διαγραφτεί γράφοντας την παρακάτω εντολή:
```
docker compose down
```

Παράδοση στον Αρίσταρχο (2η Προαιρετική Εργασία):
- Να ανεβάσετε ένα `.zip` αρχείο με όλα τα αρχεία (Dockerfile, docker-compose, source code) που χρησιμοποιήσατε για να αναπτύξετε την εργασία.
- Όνομα Αρχείου: `<Αριθμός Μητρώου>.zip` (Πχ. `e17065.zip`)