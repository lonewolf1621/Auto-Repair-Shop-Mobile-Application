from flask import Flask, request, jsonify

app = Flask(__name__)

services = [
    {"id": 1, "name": "Oil Change", "price": 50},
    {"id": 2, "name": "Brake Inspection", "price": 40}
]

bookings = []

@app.get("/services")
def get_services():
    return jsonify(services)

@app.post("/book")
def book_service():
    data = request.json
    data["id"] = len(bookings) + 1
    bookings.append(data)
    return jsonify(data), 201

@app.get("/bookings")
def get_all_bookings():
    return jsonify(bookings)

if __name__ == "__main__":
    app.run(debug=True)
