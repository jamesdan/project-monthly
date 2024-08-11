from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage (for demo purposes)
data_store = {}


# POST: Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    item_id = str(len(data_store) + 1)
    data_store[item_id] = request.json
    return jsonify({"id": item_id, "item": data_store[item_id]}), 201


# GET: Retrieve an item by ID
@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    item = data_store.get(item_id)
    if item:
        return jsonify({"id": item_id, "item": item}), 200
    else:
        return jsonify({"error": "Item not found"}), 404


# PUT: Update an item by ID
@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id in data_store:
        data_store[item_id] = request.json
        return jsonify({"id": item_id, "item": data_store[item_id]}), 200
    else:
        return jsonify({"error": "Item not found"}), 404


# DELETE: Delete an item by ID
@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id in data_store:
        deleted_item = data_store.pop(item_id)
        return jsonify({"message": "Item deleted", "item": deleted_item}), 200
    else:
        return jsonify({"error": "Item not found"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6900)
