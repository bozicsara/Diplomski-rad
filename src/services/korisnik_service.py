from sqlalchemy.exc import SQLAlchemyError
from flask_sqlalchemy.query import Query
from typing import Dict, Union, List

from .. import db
from ..model import Korisnik, KorisnikSchema
from ..util.response import Response, Status

def create(ime: str, prezime: str, email: str, broj_telefona: str) -> Response:

    if not all([ime, prezime, email, broj_telefona]):
        return Response(status=Status.Error,
                        message='Ulazi podaci za kreiranje korisnika ne smeju biti prazni!')
    

    try:
        korisnik = Korisnik(
                        ime=ime,
                        prezime=prezime,
                        email=email,
                        broj_telefona=broj_telefona
                    )
        db.session.add(korisnik)
        db.session.commit()
    except SQLAlchemyError as e:
        print(e.args)
        db.session.rollback()
        return Response(status=Status.Error,
                        message=e.args)
    
    return Response(status=Status.Success,
                    message=f'Uspseno ste kreirali korsnika {ime} {prezime}.',
                    data=KorisnikSchema(many=False).dump(korisnik))


def get_by(data: Dict[str, Union[str, int, bool]], all: bool = False) -> Union[Korisnik, List[Korisnik], None]:
    
    query:Query = Korisnik.query

    for key, value in data.items():
        if key == Korisnik.id.key:
            query = query.filter_by(id=value)
        elif key == Korisnik.ime.key:
            query = query.filter_by(ime=value)
        elif key == Korisnik.prezime.key:
            query = query.filter_by(prezime=value)
        elif key == Korisnik.email.key:
            query = query.filter_by(email=value)
        elif key == Korisnik.broj_telefona.key:
            query = query.filter_by(broj_telefona=value)
    
    if not all:
        response = query.first()
    else:
        response = query.all()    
    
    return response 