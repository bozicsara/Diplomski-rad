from flask_sqlalchemy.query import Query
from typing import Dict, Union, List

from ..model import MernaJedinica


def get_by(data: Dict[str, Union[str, int, bool]], all: bool = False) -> Union[MernaJedinica, List[MernaJedinica], None]:
    
    query:Query = MernaJedinica.query

    for key, value in data.items():
        if key == MernaJedinica.id.key:
            query = query.filter_by(id=value)
        elif key == MernaJedinica.naziv.key:
            query = query.filter_by(naziv=value)
    
    if not all:
        response = query.first()
    else:
        response = query.all()    
    
    return response


