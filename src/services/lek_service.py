from flask_sqlalchemy.query import Query
from sqlalchemy import or_, and_
from typing import Dict, Union, List

from .. import db
from ..model import Lek, Supstanca, Sadrzi, ZapakovanLek, Pakovanje, GrupaLeka, LekSchema
from ..util.response import Response, Status


def get_all() -> Response:
    data = get_by(all=True)
    return Response(status=Status.Success,
                    message=f'Uspseno ste dobavili sve lekove.',
                    data=LekSchema(many=True).dump(data))


def get_multiple_params_from_search_param(search_param:str) -> List[str]:
    return [param for param in search_param.strip().split(' ') if param != '']


def get_by_search_attribute(search_param: str) -> Response:
    if search_param == None:
        return Response(status=Status.Error,
                        message=f'Pretraga ne moze biti prazna.')
    
    if search_param == '':
        return get_all()
    
    joined_tables:Query = db.session.query(Lek)\
                                .join(Sadrzi, and_(Lek.id == Sadrzi.lek_id))\
                                .join(Supstanca, and_(Sadrzi.supstanca_id == Supstanca.id))\
                                .join(ZapakovanLek, and_(ZapakovanLek.lek_id == Lek.id))\
                                .join(Pakovanje, and_(ZapakovanLek.pakovanje_id == Pakovanje.id))\
                                .join(GrupaLeka, and_(Lek.grupa_leka_id == GrupaLeka.id))
                                    
    
    multiple_params = get_multiple_params_from_search_param(search_param=search_param)
    for search_param in multiple_params:
        query = joined_tables.filter(or_(Lek.naziv.ilike(search_param + "%"), 
                                        Supstanca.naziv.ilike(search_param + "%"),
                                        Pakovanje.vrsta.ilike(search_param + "%"),
                                        GrupaLeka.naziv.ilike(search_param + "%")))
    result = query.all()
    return Response(status=Status.Success, message='Rezultat pretrage', data=LekSchema(many=True).dump(result))




def get_by(data: Dict[str, Union[str, int, bool]] = {}, all: bool = False) -> Union[Lek, List[Lek], None]:
    
    query:Query = Lek.query

    for key, value in data.items():
        if key == Lek.id.key:
            query = query.filter_by(id=value)
        elif key == Lek.naziv.key:
            query = query.filter_by(naziv=value)
        elif key == Lek.grupa_leka_id.key:
            query = query.filter_by(grupa_leka_id=value)
    
    if not all:
        response = query.first()
    else:
        response = query.all()    
    
    return response
