import json
from enum import Enum

import jsonschema
from jsonschema import validate


class ObjectType(Enum):
    USER = "user"
    COMMENT = "comment"
    PHOTO = "photo"
    POST = "post"
    TODO = "todo"
    ALBUM = "album"


def validate_json(json_object, object_type: ObjectType):
    if isinstance(json_object, dict):
        return _validate_object(json.dumps(json_object), object_type)
    elif isinstance(json_object, list):
        for json_obj in json_object:
            if not _validate_object(json.dumps(json_obj), object_type):
                return False
        return True


def _validate_object(json_str, object_type: ObjectType):
    json_data = json.loads(json_str)
    with open(f"framework/json_schemas/{object_type.value}_schema.json",
              "rb") as schema:
        json_schema = json.load(schema)

    try:
        validate(instance=json_data, schema=json_schema)
    except jsonschema.exceptions.ValidationError:
        return False
    return True
