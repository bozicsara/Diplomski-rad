from flask import request, jsonify, Response as FlaskResponse

from .. import app
from ..services import stavka_narudzbine_service
from ..util.response import Response


base_url = '/stavka_narudzbine'


@app.route(f'{base_url}', methods=['POST'])
def create_stavka_narudzbine() -> FlaskResponse:
    zapakovan_lek_id: int = request.get_json().get('zapakovan_lek_id')
    narudzbina_id: int = request.get_json().get('narudzbina_id')
    kolicina: int = request.get_json().get('kolicina')
    
    response:Response = stavka_narudzbine_service.create(zapakovan_lek_id=zapakovan_lek_id,
                                                        narudzbina_id=narudzbina_id,
                                                        kolicina=kolicina)
    return jsonify(response.asdict())