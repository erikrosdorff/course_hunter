from flask import Flask, request
from dp import items, stores
import uuid
from flask_smorest import abort

app = Flask(__name__)

#in the 
# items = {
# 		1:	{
# 				"name": "Chair",
# 				"price": 15.99
# 			},
#             2:				{
# 				"name": "laptop",
# 				"price": 14.99
# 			}
# }

# items[1] #finds items with id 1 in dictionary
# stores = [
#     {
#         "name": "My Store",
#         "items" : [
#             {
#                 "name": "Chair",
#                 "price": 15.99
#             }
#         ]
#     }
# ]

# def my_decorator(route, fn):
#     app.routes[route] = fn
#     return fn

@app.get("/store") #http://127.0.0.1:5000/store
def get_stores():
    return {"stores" : list(stores.values())}

@app.post("/store") #posts new store
def create_store():
    store_data = request.get_json()
    if "name" not in store_data:
        abort(
            400,
            message="Bad request. Ensure 'name' is included in the JSON payload"
        )
    for store in stores.values():
        if store_data["name"] == store["name"]:
            abort(400, message=f"Store already exists")
    store_id = uuid.uuid4().hex # makes long string to make id 
    new_store = {**store_data, "id" : store_id} #collects 
    stores[store_id] = new_store
    return new_store, 201

@app.post("/item") #posts new store item
def create_item():
    item_data = request.get_json()
    if(
        "price" not in item_data
        or "store_id" not in item_data
        or "name" not in item_data
    ):
        abort(
            400,
            message="Bad Request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload. "
        )
    
    for item in item.values():
        if(
            item_data["name"] == item["name"]
            and item_data["store_id"] == item["store_id"]
        ):
            abort(400, message=f"Item already exists.")
    if item_data["store_id"] not in stores:
        abort(404, message="Store not found")
    
    item_id = uuid.uuid().hex
    item = {**item_data, "id" : item_id}
    items[item_id] = item

    return item, 201


@app.get("/store/<string:store_id>") #gets store name
def get_store(store_id):
    try:
        return stores[store_id] #gets stores by id
    except KeyError:
        abort(404, message="Store not found.")


@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found.")

@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}

# @app.get("/store") #http://127.0.0.1:5000/store
# def get_stores():
#     return {"stores" : stores}

# dict = {
#     'store': get_stores,
# }

# url = 'store'
# action = dict[url]
# action()

# @app.post("/store") #posts new store
# def create_store():
#     store_data = request.get_json()
#     store_id = uuid.uuid().hex # makes long string to make id 
#     store = {**store_data, "id" : store_id} #collects 
#     stores[store_id] = store
#     return store, 201

# @app.post("/item") #posts new store item
# def create_item():
#     item_data = request.get_json()
#     if item_data["store_id"] not in stores:
#         abort(404, message="Store not found")
    
#     item_id = uuid.uuid().hex
#     item = {**item_data, "id" : item_id}
#     items[item_id] = item

#     return item, 201

# @app.get("/store/<string:store_id>") #gets store name
# def get_store(store_id):
#     try:
#         return stores[store_id] #gets stores by id
#     except KeyError:
#         abort(404, message="Store not found")

# @app.get("/item/<string:item_id>")
# def get_item(item_id):
#     try:
#         return items[item_id]
#     except KeyError:
#         abort(404, message="item not found")

# @app.get("/item")
# def get_all_items():
#     return {"items": list(items.values())}

# # @app.post("/store") #posts new store
# # def create_store():
# #     request_data = request.get_json()
# #     new_store = {"name": request_data["name"], "items": []}
# #     stores.append(new_store)
# #     return new_store, 201

# @app.post("/item") #posts new store item
# def create_item():
#     item_data = request.get_json()
#     if item_data["store_id"] not in stores:
#         abort(404, message="Store not found")
    
#     item_id = uuid.uuid().hex
#     item = {**item_data, "id" : item_id}
#     items[item_id] = item

#     return item, 201


# # @app.post("/store/<string:name>/item") #posts new store item
# # def create_item(name):
# #     request_data = request.get_json()
# #     for store in stores:
# #         if store["name"] == name:
# #             new_item = {"name": request_data["name"], "price": request_data["price"]}
# #             store["items"].append(new_item)
# #             return new_item, 201
# #     return {"message": "Store not found"}, 404




# # @app.get("/store/<string:name>") #gets store name
# # def get_store(name):
# #     for store in stores:
# #         if store["name"] == name:
# #             return store
# #     return {"message": "Store not found"}, 404


# # @app.get("/store/<string:name>/item") #gets store item
# # def create_item(name):
# #     request_data = request.get_json()
# #     new_store = {"name": request_data["name"], "items": []}
# #     for store in stores:
# #         if store["name"] == name:
# #             new_item = {"name": request_data["name"], "price": request_data["price"]}
# #             store["items"].append(new_item)
# #             return new_item, 201
# #     return {"message": "Store not found"}, 404