from flask import request, jsonify, Response as FlaskResponse

from .. import app
from ..services import narudzbina_service
from ..util.response import Response


base_url = '/narudzbina'


@app.route(f'{base_url}', methods=['POST'])
def create_narudzbina() -> FlaskResponse:
    korisnik_id: int = request.get_json().get('korisnik_id')
    datum_vreme : float = request.get_json().get('datum_vreme')
    adresa: str = request.get_json().get('adresa')
    
    response:Response = narudzbina_service.create(korisnik_id=korisnik_id,
                                                datum_vreme=datum_vreme,
                                                adresa=adresa)
    return jsonify(response.asdict())