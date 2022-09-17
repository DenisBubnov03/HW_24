from marshmallow import Schema, fields, validates_schema, ValidationError
from typing import Any

VALID_CMD_PARAMS = (
    'filter',
    'sort',
    'map',
    'unique',
    'limit',
    'regex',
)



class RequestParams(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values: dict, *args: Any, **kwargs: Any) -> dict:
        if values['cmd'] not in VALID_CMD_PARAMS:
            raise ValidationError('"cmd" use invalid value')

        return values

class BatchRequestParams(Schema):
    queries = fields.Nested(RequestParams, many=True)
