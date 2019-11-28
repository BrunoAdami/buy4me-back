from dao import db, Base


class Deliver(Base):
    __tablename__ = 'delivers'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    score = db.Column(db.Float)
    vehicle_type = db.Column(db.String(30), nullable=False)
    vehicle_brand = db.Column(db.String(40), nullable=False)
    vehicle_year = db.Column(db.DateTime, nullable=True)
    vehicle_plate = db.Column(db.String(20), nullable=True)
    purchases = db.relationship('Purchase', back_populates='deliver')

    def __init__(self, username, email, name, score, vehicle_type,
                 vehicle_brand, vehicle_year, vehicle_plate):
        self.username = username
        self.email = email
        self.name = name
        self.score = score
        self.vehicle_type = vehicle_type
        self.vehicle_brand = vehicle_brand
        self.vehicle_year = vehicle_year
        self.vehicle_plate = vehicle_plate

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def fetch(cls):
        return cls.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
