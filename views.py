from typing import Any, is_typeddict

from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from builder import builder_query
from models import BatchRequestParams

main_bp = Blueprint('main', __name__)




@main_bp.route('/perform_query/', methods=['POST'])
def perform_query():
    try:
        params = BatchRequestParams().load(request.json)
    except ValidationError as error:
        return error.messages, 400

    results = None
    for query in params['queries']:
        results = builder_query(
            cmd=query['cmd'],
            param=query['value'],
            data=results
        )
    return jsonify(results)
