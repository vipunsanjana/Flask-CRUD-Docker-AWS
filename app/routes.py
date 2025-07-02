from flask import Blueprint, request, jsonify
from app.models import Item

bp = Blueprint('api', __name__)

@bp.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    item = Item.create(data['name'])
    return jsonify(item), 201

@bp.route('/items', methods=['GET'])
def list_items():
    return jsonify(Item.list_all())

@bp.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.read(item_id)
    return (jsonify(item), 200) if item else ('Not found', 404)

@bp.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    item = Item.update(item_id, data['name'])
    return (jsonify(item), 200) if item else ('Not found', 404)

@bp.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.delete(item_id)
    return (jsonify(item), 200) if item else ('Not found', 404)
