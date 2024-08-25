from src import app, db, socketio
from src.initial_data import create_grupa_leka_entities, create_supstanca_entities, create_pakovanje_entities, create_merna_jedinica_entities, create_korisnik_entities, create_lek_entities, create_sadrzi_entities, create_narudzbina_entities, create_zapakovan_lek_entities, create_stavka_narudzbine_entities


def create_inital_data():
    create_grupa_leka_entities()
    create_supstanca_entities()
    create_pakovanje_entities()
    create_merna_jedinica_entities()
    create_korisnik_entities()
    create_lek_entities()
    create_sadrzi_entities()
    create_narudzbina_entities()
    create_zapakovan_lek_entities()
    create_stavka_narudzbine_entities()


if __name__ == "__main__": 
    db.drop_all()
    db.create_all()
    
    create_inital_data()
    
    socketio.run(app, debug=True, use_reloader=False, port=5000)
