from dao import db, Base


class Client(Base):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    purchases = db.relationship('Purchase', bask_populates='client')

    def __init__(self, username, email, name):
        self.username = username
        self.email = email
        self.name = name

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


# We don't need to define a __init__ method because SQLAlchemy adds an
# implicit constructor to all model classes which accepts keyword arguments
# for all its columns and relationships.
