from flask import request, jsonify, Response as FlaskResponse

from .. import app
from ..services import zapakovan_lek_service
from ..util.response import Response


base_url = '/zapakovan_lek'


@app.route(f'{base_url}', methods=['PATCH'])
def update_zaliha_in_entity_zapakovan_lek() -> Response:
    id: int = request.get_json().get('id')
    zatrazena_kolicina: int = request.get_json().get('zatrazena_kolicina')
    
    response:Response = zapakovan_lek_service.update_zalihe(id=id,
                                                            zatrazena_kolicina=zatrazena_kolicina)
    return jsonify(response.asdict())