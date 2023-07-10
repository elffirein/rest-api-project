import uuid
from flask import Flask, jsonify, request
from flask_smorest import abort
from db import stores, items
import json


app = Flask(__name__)


@app.route("/store")
def get_stores():
    return {"stores": list(stores.values())}


@app.route("/store", methods=['POST'])
def create_store():
    store_data = request.get_json()

    if "name" not in store_data:
        abort(400,
              message="Bad Request: Ensure 'name' is included in JSON payload"
              )

    for store in stores.values():
        if store["name"] == store_data["name"]:
            abort(400, message=f"Store {store_data['name']} already exists")

    store_id = uuid.uuid4().hex
    new_store = {**store_data, "id": store_id}
    stores[store_id] = new_store
    return new_store, 201


@app.route("/store/<string:store_id>", methods=["GET"])
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found")


@app.route("/store/<string:store_id>", methods=["DELETE"])
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message": f"store {store_id} got deleted"}
    except KeyError:
        abort(404, message=f"Store {store_id} not found")


@app.route("/item", methods=['POST'])
def create_item():
    item_data = request.get_json()

    if item_data["store_id"] not in stores.keys():
        abort(404, message="Store not found")

    if "price" not in item_data or "store_id" not in item_data or "name" not in item_data:
        abort(400,
              message="Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload.",
            )

    for item in items.values():
        if item_data["name"] == item["name"] and item_data["store_id"] == item["store_id"]:
            abort(400, message=f"Item already exists.")

    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item
    return item, 201


@app.route("/items", methods=['GET'])
def get_all_items():
    return {"items": list(items.values())}


@app.route("/item/<string:item_id>", methods=['GET'])
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found")


@app.route("/item/<string:item_id>", methods=['DELETE'])
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message": f"Item {item_id} got deleted"}
    except KeyError:
        abort(404, message=f"item {item_id} not found")


