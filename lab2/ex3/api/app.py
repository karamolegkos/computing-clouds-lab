import os
from io import BytesIO
from flask import (
    Flask,
    request,
    jsonify,
    send_file,
    render_template,
    redirect,
    url_for,
    flash,
)
from minio import Minio
from minio.error import S3Error

app = Flask(__name__)
app.secret_key = "change-this-secret"  # βάλε κάτι δικό σου

MINIO_ENDPOINT = os.environ.get("MINIO_ENDPOINT", "minio:9000")
MINIO_ACCESS_KEY = os.environ.get("MINIO_ACCESS_KEY", "minioadmin")
MINIO_SECRET_KEY = os.environ.get("MINIO_SECRET_KEY", "minioadmin123")
MINIO_BUCKET = os.environ.get("MINIO_BUCKET", "files")

minio_client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False,  # http, όχι https
)

# Δημιουργία bucket αν δεν υπάρχει
found = minio_client.bucket_exists(MINIO_BUCKET)
if not found:
    minio_client.make_bucket(MINIO_BUCKET)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


# ---------- UI ROUTES ----------

@app.route("/", methods=["GET", "POST"])
def index():
    """
    UI:
    - GET: δείχνει φόρμα για upload + λίστα αρχείων
    - POST: ανεβάζει αρχείο και επιστρέφει πάλι στη σελίδα
    """
    if request.method == "POST":
        if "file" not in request.files:
            flash("Δεν βρέθηκε αρχείο στο request", "error")
            return redirect(url_for("index"))

        file = request.files["file"]

        if file.filename == "":
            flash("Δεν επέλεξες αρχείο", "error")
            return redirect(url_for("index"))

        try:
            data = file.read()
            file_size = len(data)

            minio_client.put_object(
                bucket_name=MINIO_BUCKET,
                object_name=file.filename,
                data=BytesIO(data),
                length=file_size,
                content_type=file.content_type or "application/octet-stream",
            )

            flash(f"Το αρχείο '{file.filename}' ανέβηκε επιτυχώς!", "success")
            return redirect(url_for("index"))

        except S3Error as e:
            flash(f"Σφάλμα κατά το upload: {str(e)}", "error")
            return redirect(url_for("index"))

    # GET: φέρνουμε λίστα αρχείων από MinIO
    files = []
    try:
        objects = minio_client.list_objects(MINIO_BUCKET, recursive=True)
        for obj in objects:
            files.append(
                {
                    "name": obj.object_name,
                    "size": obj.size,
                }
            )
    except S3Error as e:
        flash(f"Σφάλμα κατά το list: {str(e)}", "error")

    return render_template("index.html", files=files)


# ---------- API ROUTES ----------

@app.route("/upload", methods=["POST"])
def upload_file():
    """API για upload (χωρίς UI, χρήσιμο για scripts / curl)."""
    if "file" not in request.files:
        return jsonify({"error": "No file part in request"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    try:
        data = file.read()
        file_size = len(data)

        minio_client.put_object(
            bucket_name=MINIO_BUCKET,
            object_name=file.filename,
            data=BytesIO(data),
            length=file_size,
            content_type=file.content_type or "application/octet-stream",
        )

        return jsonify({"message": "File uploaded", "filename": file.filename}), 201

    except S3Error as e:
        return jsonify({"error": str(e)}), 500


@app.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    """Κατεβάζει αρχείο από MinIO με το δοσμένο filename."""
    try:
        response = minio_client.get_object(MINIO_BUCKET, filename)
        data = response.read()
        response.close()
        response.release_conn()

        return send_file(
            BytesIO(data),
            as_attachment=True,
            download_name=filename,
        )
    except S3Error as e:
        if e.code == "NoSuchKey":
            return jsonify({"error": "File not found"}), 404
        return jsonify({"error": str(e)}), 500


@app.route("/list", methods=["GET"])
def list_files():
    """Επιστρέφει λίστα με όλα τα objects του bucket (JSON)."""
    try:
        objects = minio_client.list_objects(MINIO_BUCKET, recursive=True)
        files = [{"name": obj.object_name, "size": obj.size} for obj in objects]
        return jsonify(files), 200
    except S3Error as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)