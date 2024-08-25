from flask import request, jsonify, Response as FlaskResponse

from .. import app
from ..services import korisnik_service
from ..util.response import Response


base_url = '/korisnik'


@app.route(f'{base_url}', methods=['POST'])
def create_korisnik() -> FlaskResponse:
    ime: str = request.get_json().get('ime')
    prezime: str = request.get_json().get('prezime')
    email: str = request.get_json().get('email')
    broj_telefona: str = request.get_json().get('broj_telefona')
    
    response:Response = korisnik_service.create(ime=ime,
                                                prezime=prezime,
                                                email=email,
                                                broj_telefona=broj_telefona)
    return jsonify(response.asdict())