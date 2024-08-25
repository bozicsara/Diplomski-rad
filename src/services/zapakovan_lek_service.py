from sqlalchemy.exc import SQLAlchemyError
from flask_sqlalchemy.query import Query
from typing import Dict, Union, List

from .. import db, lock
from ..model import ZapakovanLek, ZapakovanLekSchema
from ..services import lek_service, merna_jedinica_service, pakovanje_service
from ..util.response import Response, Status


def create(lek_id: int, merna_jedinica_id: int, pakovanje_id: int) -> Response:
    
    if lek_id == None or lek_id == -1 or merna_jedinica_id == None or \
        merna_jedinica_id == -1 or pakovanje_id == None or pakovanje_id == -1:
        return Response(status=Status.Error,
                        message='Ulazi podaci za kreiranje zapakovanog leka ne smeju biti prazni!')
    
    if not lek_service.get_by(data={'id': lek_id}):
        return Response(status=Status.Error,
                        message=f'Lek sa id-em {lek_id} ne postoji.')
    
    if not merna_jedinica_service.get_by(data={'id': merna_jedinica_id}):
        return Response(status=Status.Error,
                        message=f'Merna jedinica sa id-em {merna_jedinica_id} ne postoji.')
    
    if not pakovanje_service.get_by(data={'id': pakovanje_id}):
        return Response(status=Status.Error,
                        message=f'Pakovanje sa id-em {pakovanje_id} ne postoji.')
    
    try:
        zapakovan_lek = ZapakovanLek(
                        lek_id=lek_id,
                        merna_jedinica_id=merna_jedinica_id,
                        pakovanje_id=pakovanje_id
                    )
        db.session.add(zapakovan_lek)
        db.session.commit()
    except SQLAlchemyError as e:
        print(e.args)
        db.session.rollback()
        return Response(status=Status.Error,
                        message=e.args)
    
    return Response(status=Status.Success,
                    message=f'Uspseno ste kreirali zapakovan lek.',
                    data=ZapakovanLekSchema(many=False).dump(zapakovan_lek))


def update_zalihe(id: int, zatrazena_kolicina: int) -> Response:
    if id == None or id == -1 or zatrazena_kolicina == None or zatrazena_kolicina <= 0:
        return Response(status=Status.Error,
                        message='Ulazni podaci za izmenu zaliha zapakovanog leka ne smeju biti prazni!')
    
    lock.acquire()

    zapakovan_lek = get_by(data={'id': id})
    if not zapakovan_lek:
        lock.release()
        return Response(status=Status.Error,
                        message=f'Zapakovan lek sa id-em {id} ne postoji.')
    
    
    if zapakovan_lek.zaliha < zatrazena_kolicina:
        lock.release()
        return Response(status=Status.Error,
                        message=f'Zatrazena kolicina zapakovanog leka {zatrazena_kolicina} sa id-em {id} ne moze biti manja od trenutne zalihe {zapakovan_lek.zaliha}.')


    try:
        zapakovan_lek.zaliha = zapakovan_lek.zaliha - zatrazena_kolicina
        db.session.commit()
    except SQLAlchemyError as e:
        print(e.args)
        db.session.rollback()
        return Response(status=Status.Error,
                        message=e.args)
    finally:
        lock.release()
    
    return Response(status=Status.Success,
                    message=f'Uspeseno ste izmenili zalihu zapakovanog leka.',
                    data=ZapakovanLekSchema(many=False).dump(zapakovan_lek))


def get_by(data: Dict[str, Union[str, int, bool]], all: bool = False) -> Union[ZapakovanLek, List[ZapakovanLek], None]:
    
    query:Query = ZapakovanLek.query

    for key, value in data.items():
        if key == ZapakovanLek.id.key:
            query = query.filter_by(id=value)
        elif key == ZapakovanLek.lek_id.key:
            query = query.filter_by(lek_id=value)
        elif key == ZapakovanLek.merna_jedinica_id.key:
            query = query.filter_by(merna_jedinica_id=value)
        elif key == ZapakovanLek.pakovanje_id.key:
            query = query.filter_by(pakovanje_id=value)
    
    if not all:
        response = query.first()
    else:
        response = query.all()    
    
    return response 
