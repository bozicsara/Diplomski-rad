from flask import request, jsonify, Response as FlaskResponse

from .. import app
from ..services import lek_service
from ..util.response import Response


base_url = '/lek'


@app.route(f'{base_url}/all', methods=['GET'])
def get_all_enitites_of_type_lek() -> FlaskResponse:
    response:Response = lek_service.get_all()
    return jsonify(response.asdict())


@app.route(f'{base_url}', methods=['GET'])
def get_specific_enitites_of_type_lek() -> FlaskResponse:
    search_param: str = request.args.get('search_param')
    response:Response = lek_service.get_by_search_attribute(search_param=search_param)
    return jsonify(response.asdict())