# Εγκατάσταση και χρήση του Jupyter Notebook μέσω Docker

## Εγκατάσταση
Για να κατεβάσετε και να εκκινήσετε ένα container με **Jupyter Notebook** εκτελέστε:
```shell
# Windows
docker run --name my-jupyter ^
  -p 8888:8888 ^
  -v ./notebooks:/home/jovyan/work ^
  -d jupyter/base-notebook

# Linux
docker run --name my-jupyter \
  -p 8888:8888 \
  -v ./notebooks:/home/jovyan/work \
  -d jupyter/base-notebook
```

Στην παραπάνω εντολή χρησιμοποιούνται τα εξής:
- `--name my-jupyter`: Το όνομα του container (μπορείτε να το αλλάξετε).
- `-p 8888:8888`: Εκθέτει την πόρτα 8888 του container (όπου τρέχει ο Jupyter) στην ίδια πόρτα του host.
- `-v ./notebooks:/home/jovyan/work`: Κάνει mount έναν τοπικό φάκελο ./notebooks για αποθήκευση των αρχείων σας (ώστε να μην χαθούν αν διαγραφεί το container).
- `-d`: Εκτελεί το container στο παρασκήνιο (detached mode).
- `jupyter/base-notebook`: Χρησιμοποιεί το επίσημο image της Jupyter.

## Πρόσβαση στο Jupyter Notebook UI
Αφού ξεκινήσει το container, μπορείτε να δείτε τα logs του για να βρείτε το URL σύνδεσης με token:
```shell
docker logs my-jupyter
```

Θα δείτε κάτι σαν:
```
Or copy and paste one of these URLs:
    http://127.0.0.1:8888/lab?token=abcdef123456789...
```

Ανοίξτε αυτό το URL στον browser σας για να αποκτήσετε πρόσβαση στο **Jupyter Notebook / JupyterLab UI**.

## Εναλλακτικά: Ορισμός Σταθερού Κωδικού Αντί για Token
Αν προτιμάτε να χρησιμοποιείτε password αντί για token, μπορείτε να εκκινήσετε το container με επιπλέον μεταβλητή περιβάλλοντος:
```shell
# For Windows
docker run --name my-jupyter ^
  -p 8888:8888 ^
  -v ./notebooks:/home/jovyan/work ^
  -e JUPYTER_TOKEN=mytoken123 ^
  -d jupyter/base-notebook
```

Τώρα μπορείτε να συνδεθείτε στο: http://localhost:8888, Χρησιμοποιώντας ως token ή password το `mytoken123`.

# **✅ Συμπεράσματα**
Με αυτό το setup μπορείτε:
- Να εκτελέσετε εύκολα έναν Jupyter Notebook server μέσω Docker.
- Να έχετε πρόσβαση στο περιβάλλον εργασίας μέσω browser στο http://localhost:8888.
- Να αποθηκεύετε τα αρχεία σας τοπικά για μόνιμη χρήση.