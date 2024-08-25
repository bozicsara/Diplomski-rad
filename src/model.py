from src import db, ma
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.types import DECIMAL
from marshmallow import fields


class Sadrzi(db.Model):
    __tablename__ = 'sadrzi'
    
    lek_id = db.Column(
        db.Integer, ForeignKey('lek.id'), primary_key=True)
    supstanca_id = db.Column(
        db.Integer, ForeignKey('supstanca.id'), primary_key=True)

class ZapakovanLek(db.Model):
    __tablename__ = 'zapakovan_lek'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    lek_id = db.Column(
        db.Integer, ForeignKey('lek.id'), nullable=False)
    merna_jedinica_id = db.Column(
        db.Integer, ForeignKey('merna_jedinica.id'), nullable=False)
    pakovanje_id = db.Column(
        db.Integer, ForeignKey('pakovanje.id'), nullable=False)
    
    zaliha = db.Column(db.Integer, nullable=False)
    jacina = db.Column(db.String(512), nullable=False)
    kolicina = db.Column(db.Integer, nullable=False)
    cena = db.Column(DECIMAL(scale=2), nullable=False)
    url = db.Column(db.String(512), nullable=False)
    
    narudzbine = db.relationship('StavkaNarudzbine',
                            backref='zapakovan_lek_',
                            lazy='dynamic'
                            )


class StavkaNarudzbine(db.Model):
    __tablename__ = 'stavka_narudzbine'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    zapakovan_lek_id = db.Column(
        db.Integer, ForeignKey('zapakovan_lek.id'), nullable=False)
    narudzbina_id = db.Column(
        db.Integer, ForeignKey('narudzbina.id'), nullable=False)
    
    kolicina = db.Column(db.Integer, nullable=False)


class Korisnik(db.Model):
    __tablename__ = 'korisnik'
    
    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(30), nullable=False)
    prezime = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    broj_telefona = db.Column(db.String(20), nullable=False)

    narudzbine = db.relationship('Narudzbina',
                            backref='korisnik_',
                            lazy='dynamic'
                            )


class Narudzbina(db.Model):
    __tablename__ = 'narudzbina'
    
    id = db.Column(db.Integer, primary_key=True)

    korisnik_id = db.Column(db.Integer, db.ForeignKey('korisnik.id'), nullable=False)

    datum = db.Column(db.Date, nullable=False)
    vreme = db.Column(db.Time, nullable=False)
    adresa = db.Column(db.String(100), nullable=False)
    
    zapakovani_lekovi = db.relationship('StavkaNarudzbine',
                            backref='narudzbina_',
                            lazy='dynamic'
                            )


class Supstanca(db.Model):
    __tablename__ = 'supstanca'
    
    id = db.Column(db.Integer, primary_key=True)
    
    naziv = db.Column(db.String(50), nullable=False)

    lekovi = db.relationship('Sadrzi',
                            backref='supstanca_',
                            lazy='dynamic'
                            )


class GrupaLeka(db.Model):
    __tablename__ = 'grupa_leka'
    
    id = db.Column(db.Integer, primary_key=True)
    
    naziv = db.Column(db.String(30), nullable=False)
    
    lekovi = db.relationship('Lek',
                            backref='grupa_leka_',
                            lazy='dynamic'
                            )


class MernaJedinica(db.Model):
    __tablename__ = 'merna_jedinica'
    
    id = db.Column(db.Integer, primary_key=True)

    naziv = db.Column(db.String(20), nullable=False)
    zapakovani_lekovi = db.relationship('ZapakovanLek',
                                backref='merna_jedinica_',
                                lazy='dynamic'
                                )


class Pakovanje(db.Model):
    __tablename__ = 'pakovanje'
    
    id = db.Column(db.Integer, primary_key=True)

    vrsta = db.Column(db.String(30), nullable=False)
    zapakovani_lekovi = db.relationship('ZapakovanLek',
                                backref='pakovanje_',
                                lazy='dynamic'
                                )


class Lek(db.Model):
    __tablename__ = 'lek'
    
    id = db.Column(db.Integer, primary_key=True)

    grupa_leka_id = db.Column(db.Integer, db.ForeignKey('grupa_leka.id'), nullable=False)

    naziv = db.Column(db.String(100), nullable=False)
    opis_namena = db.Column(db.Text, nullable=False)
    doziranje = db.Column(db.Text, nullable=False)
    nezeljena_dejstva = db.Column(db.Text, nullable=False)
    susptance = db.relationship('Sadrzi',
                                backref='lek_',
                                lazy='dynamic'
                                )
    zapakovani_lekovi = db.relationship('ZapakovanLek',
                                backref='lek_',
                                lazy='dynamic'
                                )


############### Marshmallow classes ###############

class SupstancaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Supstanca
    
    id = ma.auto_field()
    naziv = ma.auto_field()

    lekovi = fields.List(fields.Nested(lambda: SadrziSchema(exclude=('supstanca_', ))))


class GrupaLekaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = GrupaLeka
    
    id = ma.auto_field()
    naziv = ma.auto_field()

    lekovi = fields.List(fields.Nested(lambda: LekSchema(exclude=('grupa_leka_', 'supstance', 'zapakovani_lekovi', ))))


class MernaJedinicaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = MernaJedinica
    
    id = ma.auto_field()
    naziv = ma.auto_field()

    zapakovani_lekovi = fields.List(fields.Nested(lambda: ZapakovanLekSchema(only=('id', ))))


class StavkaNarudzbineSchema(ma.SQLAlchemySchema):
    class Meta:
        model = StavkaNarudzbine
    
    id = ma.auto_field()
    kolicina = ma.auto_field()

    zapakovani_lek_ = fields.Nested(lambda: ZapakovanLekSchema(only=('id', )))
    narudzbina_ = fields.Nested(lambda: NarudzbinaSchema(exclude=('korisnik_', 'zapakovani_lekovi', )))


class NarudzbinaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Narudzbina
    
    id = ma.auto_field()
    datum = ma.auto_field()
    vreme = ma.auto_field()
    adresa = ma.auto_field()

    korisnik_ = fields.Nested(lambda: KorisnikSchema(exclude=('narudzbine', )))
    zapakovani_lekovi = fields.List(fields.Nested(lambda: StavkaNarudzbineSchema(exclude=('narudzbina_', ))))


class PakovanjeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Pakovanje
    
    id = ma.auto_field()
    vrsta = ma.auto_field()

    zapakovani_lekovi = fields.List(fields.Nested(lambda: ZapakovanLekSchema(only=('id', ))))


class KorisnikSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Korisnik
    
    id = ma.auto_field()
    ime = ma.auto_field()
    prezime = ma.auto_field()
    email = ma.auto_field()
    broj_telefona = ma.auto_field()

    narudzbine = fields.List(fields.Nested(NarudzbinaSchema(exclude=('korisnik_', 'zapakovani_lekovi', ))))


class ZapakovanLekSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ZapakovanLek
    
    id = ma.auto_field()
    zaliha = ma.auto_field()
    jacina = ma.auto_field()
    kolicina = ma.auto_field()
    cena = ma.auto_field()
    url = ma.auto_field()
    lek_ = fields.Nested(lambda: LekSchema(exclude=('grupa_leka_', 'susptance', 'zapakovani_lekovi', )))
    merna_jedinica_ = fields.Nested(MernaJedinicaSchema(exclude=('zapakovani_lekovi', )))
    pakovanje = fields.Nested(PakovanjeSchema(exclude=('zapakovani_lekovi', )))

    narudzbine = fields.List(fields.Nested(StavkaNarudzbineSchema(exclude=('zapakovani_lek_', ))))


class SadrziSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Sadrzi
    
    lek_ = fields.Nested(lambda: LekSchema(exclude=('grupa_leka_', 'susptance', 'zapakovani_lekovi', )))
    supstanca_ = fields.Nested(SupstancaSchema(exclude=('lekovi', )))


class LekSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Lek
    
    id = ma.auto_field()
    naziv = ma.auto_field()
    opis_namena = ma.auto_field()
    doziranje = ma.auto_field()
    nezeljena_dejstva = ma.auto_field()

    grupa_leka_ = fields.Nested(GrupaLekaSchema(exclude=('lekovi', )))
    susptance = fields.List(fields.Nested(SadrziSchema(exclude=('lek_', ))))
    zapakovani_lekovi = fields.List(fields.Nested(ZapakovanLekSchema(only=('id', 'url', 'cena', 'zaliha', 'jacina', 'merna_jedinica_', ))))


