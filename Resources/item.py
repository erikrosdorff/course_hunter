import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from dp import items
from schemas import ItemSchemas, ItemUpdateSchema


blp = Blueprint("items", __name__, description="Operations on items")

@blp.route("/item/<string:item_id>")
class item(MethodView):
    @blp.response(200, ItemSchemas)
    def get(self, item_id):
        try:
            return items[item_id] #gets items by id
        except KeyError:
            abort(404, message="item not found.")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "item deleted"}
        except KeyError:
            abort(404, message="item not found.")
    
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchemas)
    def put(self, item_data, item_id):

        try:
            item = items[item_id]

            item | item_data

            return item
        except KeyError:
            abort(404, message="Item not found")
@blp.route("/item")
class itemList(MethodView):
    @blp.response(200, ItemSchemas(many=True)) #returns a list
    def get(self):
        return items.values()
    @blp.arguments(ItemSchemas)
    @blp.response(200, ItemSchemas)
    def post(self, item_data):
        for item in items.values():
            if(
                item_data["name"] == item["name"]
                and item_data["item_id"] == item["item_id"]
            ):
                abort(400, message=f"item already exists.")
        
        
        item_id = uuid.uuid4().hex
        item = {**item_data, "id" : item_id}
        items[item_id] = item

        return item
