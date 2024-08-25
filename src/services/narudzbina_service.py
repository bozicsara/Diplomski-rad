from sqlalchemy.exc import SQLAlchemyError
from flask_sqlalchemy.query import Query
from typing import Dict, Union, List
from datetime import date, time

from .. import db
from ..model import Narudzbina, NarudzbinaSchema
from ..services import korisnik_service
from ..util import date_time_helper
from ..util.response import Response, Status

def create(korisnik_id: int, datum_vreme: float, adresa: str) -> Response:

    if korisnik_id == None or korisnik_id == -1 or datum_vreme == None or \
        adresa == None or adresa == '':
        return Response(status=Status.Error,
                        message='Ulazi podaci za kreiranje narudzbine ne smeju biti prazni!')
    
    if not korisnik_service.get_by(data={'id': korisnik_id}):
        return Response(status=Status.Error,
                        message=f'Korisnik sa id-em {korisnik_id} ne postoji.')
    
    datum: date = date_time_helper.get_date_by_timestamp(datum_vreme)
    vreme: time = date_time_helper.get_time_by_timestamp(datum_vreme)

    try:
        narudzbina = Narudzbina(
                        korisnik_id=korisnik_id,
                        datum=datum,
                        vreme=vreme,
                        adresa=adresa
                    )
        db.session.add(narudzbina)
        db.session.commit()
    except SQLAlchemyError as e:
        print(e.args)
        db.session.rollback()
        return Response(status=Status.Error,
                        message=e.args)
    
    return Response(status=Status.Success,
                    message=f'Uspseno ste kreirali narudzbinu.',
                    data=NarudzbinaSchema(many=False).dump(narudzbina))


def get_by(data: Dict[str, Union[str, int, bool]], all: bool = False) -> Union[Narudzbina, List[Narudzbina], None]:
    
    query:Query = Narudzbina.query

    for key, value in data.items():
        if key == Narudzbina.id.key:
            query = query.filter_by(id=value)
        elif key == Narudzbina.korisnik_id.key:
            query = query.filter_by(korisnik_id=value)
        elif key == Narudzbina.datum.key:
            query = query.filter_by(datum=value)
        elif key == Narudzbina.vreme.key:
            query = query.filter_by(vreme=value)
        elif key == Narudzbina.adresa.key:
            query = query.filter_by(adresa=value)
    
    if not all:
        response = query.first()
    else:
        response = query.all()    
    
    return response 