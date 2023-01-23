from flask import Flask 

flask_api = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items" : [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]

@flask_api.get("/store")


def get_stores():
    return {"stores" : stores}