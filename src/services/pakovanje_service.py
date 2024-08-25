from flask_sqlalchemy.query import Query
from typing import Dict, Union, List

from ..model import Pakovanje


def get_by(data: Dict[str, Union[str, int, bool]], all: bool = False) -> Union[Pakovanje, List[Pakovanje], None]:
    
    query:Query = Pakovanje.query

    for key, value in data.items():
        if key == Pakovanje.id.key:
            query = query.filter_by(id=value)
        elif key == Pakovanje.vrsta.key:
            query = query.filter_by(vrsta=value)
    
    if not all:
        response = query.first()
    else:
        response = query.all()    
    
    return response