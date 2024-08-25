from sqlalchemy.exc import SQLAlchemyError
from flask_sqlalchemy.query import Query
from typing import Dict, Union, List

from . import zapakovan_lek_service

from .. import db
from ..model import StavkaNarudzbine, StavkaNarudzbineSchema
from ..services import narudzbina_service
from ..util.response import Response, Status


def create(zapakovan_lek_id: int, narudzbina_id: int, kolicina: int) -> Response:
    
    if zapakovan_lek_id == None or zapakovan_lek_id == -1 or narudzbina_id == None or \
        narudzbina_id == -1 or kolicina == None or kolicina < 1:
        return Response(status=Status.Error,
                        message='Ulazi podaci za kreiranje stavke narudzbine ne smeju biti prazni!')
    
    updateKolicine = zapakovan_lek_service.update_zalihe(zapakovan_lek_id, kolicina)
    if updateKolicine.status == Status.Error:
        return updateKolicine
    
    if not narudzbina_service.get_by(data={'id': narudzbina_id}):
        return Response(status=Status.Error,
                        message=f'Narudzbina sa id-em {narudzbina_id} ne postoji.')
    
    if not zapakovan_lek_service.get_by(data={'id': zapakovan_lek_id}):
        return Response(status=Status.Error,
                        message=f'Zapakovan lek sa id-em {zapakovan_lek_id} ne postoji.')
    
    try:
        stavka_narudzbine = StavkaNarudzbine(
                        zapakovan_lek_id=zapakovan_lek_id,
                        narudzbina_id=narudzbina_id,
                        kolicina=kolicina
                    )
        db.session.add(stavka_narudzbine)
        db.session.commit()
    except SQLAlchemyError as e:
        print(e.args)
        db.session.rollback()
        return Response(status=Status.Error,
                        message=e.args)
    
    return Response(status=Status.Success,
                    message=f'Uspseno ste kreirali stavku narudzbine.',
                    data=StavkaNarudzbineSchema(many=False).dump(stavka_narudzbine))


def get_by(data: Dict[str, Union[str, int, bool]], all: bool = False) -> Union[StavkaNarudzbine, List[StavkaNarudzbine], None]:
    
    query:Query = StavkaNarudzbine.query

    for key, value in data.items():
        if key == StavkaNarudzbine.id.key:
            query = query.filter_by(id=value)
        elif key == StavkaNarudzbine.zapakovan_lek_id.key:
            query = query.filter_by(zapakovan_lek_id=value)
        elif key == StavkaNarudzbine.narudzbina_id.key:
            query = query.filter_by(narudzbina_id=value)
        elif key == StavkaNarudzbine.kolicina.key:
            query = query.filter_by(kolicina=value)
    
    if not all:
        response = query.first()
    else:
        response = query.all()    
    
    return response

    