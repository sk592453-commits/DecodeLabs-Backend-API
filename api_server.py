from flask import Flask, jsonify, request

# 1. Initialize Flask App (This line is most important)
app = Flask(__name__)

# Fake Database for DecodeLabs Project
inventory_items = [
    {"id": 101, "name": "Standard Package", "category": "Logistics", "status": "In-Transit"},
    {"id": 102, "name": "Premium Kit", "category": "Training", "status": "Delivered"}
]

# 2. GET Method
@app.route('/items', methods=['GET'])
def get_all_items():
    return jsonify({
        "status": "Success",
        "count": len(inventory_items),
        "resources": inventory_items
    }), 200

# 3. POST Method with Gatekeeper Validation
@app.route('/items', methods=['POST'])
def create_new_item():
    payload = request.json

    if not payload or "name" not in payload or "category" not in payload:
        return jsonify({
            "error": "Bad Request",
            "message": "Validation Failed! 'name' and 'category' are mandatory."
        }), 400

    new_resource = {
        "id": inventory_items[-1]["id"] + 1 if inventory_items else 101,
        "name": payload["name"].strip(),
        "category": payload["category"].strip(),
        "status": payload.get("status", "Pending")
    }
    inventory_items.append(new_resource)

    return jsonify({
        "status": "Created",
        "resource": new_resource
    }), 201

# 4. Run the Application
if __name__ == '__main__':
    app.run(debug=True, port=5000)
