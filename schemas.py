from marshmallow import Schema, fields

class PlainItemSchemas(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)



class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class ItemSchema(PlainItemSchemas):
    store_id = fields.Int(required = True, load_only = True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchemas()), dunmp_only=True)

