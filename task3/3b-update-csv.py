from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

CSV_FILE = "posts.csv"

def load_csv():
    data = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
    return data

def save_csv(data):
    with open(CSV_FILE, "w", newline="") as csv_file:
        fieldnames = ["userId", "id", "title", "body"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(data)

@app.route("/api/records", methods=["GET"])
def get_records():
    data = load_csv()
    return jsonify(data)

@app.route("/api/record/<int:user_id>", methods=["POST", "PATCH"])
def update_record(user_id):
    data = load_csv()

    record = next((item for item in data if item["userId"] == str(user_id)), None)

    if request.method == "POST":
        new_record = {
            "userId": str(user_id),
            "id": request.json["id"],
            "title": request.json["title"],
            "body": request.json["body"]
        }
        if record is None:
            data.append(new_record)
        else:
            return jsonify({"message": "Record already exists. Use PATCH to update."}), 400

    elif request.method == "PATCH":
        if record:
            record.update(request.json)
        else:
            return jsonify({"message": "Record not found."}), 404

    save_csv(data)
    return jsonify({"message": "Record updated successfully."})

if __name__ == "__main__":
    app.run(debug=True)
