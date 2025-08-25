from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = "supersecret"

# FastAPI Base URL
FASTAPI_URL = "http://127.0.0.1:8000"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add-room", methods=["GET", "POST"])
def add_room():
    if request.method == "POST":
        name = request.form["name"]
        capacity = int(request.form["capacity"])
        room_data = {"name": name, "capacity": capacity}
        res = requests.post(f"{FASTAPI_URL}/rooms/", json=room_data)

        if res.status_code == 200:
            flash("Room added successfully!", "success")
        else:
            flash("Failed to add room.", "error")

        return redirect(url_for("add_room"))
    return render_template("add_room.html")

@app.route("/book-room", methods=["GET", "POST"])
def book_room():
    if request.method == "POST":
        customer_name = request.form["customer_name"]
        room_id = int(request.form["room_id"])

        # First create the customer
        customer_res = requests.post(f"{FASTAPI_URL}/customers/", json={"name": customer_name})
        if customer_res.status_code != 200:
            flash("Failed to create customer", "error")
            return redirect(url_for("book_room"))

        customer_id = customer_res.json()["id"]

        # Then book the room
        booking_res = requests.post(f"{FASTAPI_URL}/bookings/", json={"customer_id": customer_id, "room_id": room_id})
        if booking_res.status_code == 200 and booking_res.json()["status"] == "success":
            flash("Room booked successfully!", "success")
        else:
            flash("Failed to book room. " + booking_res.json().get("message", ""), "error")

        return redirect(url_for("book_room"))

    # Get available rooms
    rooms_res = requests.get(f"{FASTAPI_URL}/rooms/available")
    rooms = rooms_res.json() if rooms_res.status_code == 200 else []
    return render_template("book_room.html", rooms=rooms)

if __name__ == "__main__":
    app.run(debug=True)
