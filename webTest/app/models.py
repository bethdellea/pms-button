from app import db
import datetime


class State(db.Model):
    __tablename__ = 'state'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String)
    abbr = db.Column(db.String(2))

    def __init__(self, full_name, abbr):
        self.full_name = full_name
        self.abbr = abbr


class District(db.Model):
    __tablename__ = 'district'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    state_id = db.Column(db.Integer, db.ForeignKey('state.id'))
    state = db.relationship('state', foreign_keys=[state_id])

    def __init__(self, state, number):
        self.state = state
        self.number = number


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    pass_hash = db.Column(db.String)
    zip_code = db.Column(db.String(5))
    last_push = db.Column(db.DateTime)
    email = db.Column(db.String(64))

    state_id = db.Column(db.Integer, db.ForeignKey('state.id'))
    state = db.relationship('state', foreign_keys=[state_id])
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))
    district = db.relationship('district', foreign_keys=[district_id])

    def __init__(self, username, pass_hash, zip_code, email):
        self.username = username
        self.pass_hash = pass_hash
        self.zip_code = zip_code
        self.email = email

        # TODO: magical zip code to state/district logic
        self.state = None
        self.district = None

    def update_push_time(self):
        self.last_push = datetime.datetime.utcnow()

    def can_push(self):
        return datetime.datetime.utcnow() - self.last_push >= datetime.timedelta(days=1)


class Congressperson(db.Model):
    __tablename__ = 'congressperson'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    twitter = db.Column(db.String)
    desc = db.Column(db.String)
    photo_url = db.Colume(db.String)

    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))
    district = db.relationship('district', foreign_keys=[district_id])
    state_id = db.Column(db.Integer, db.ForeignKey('state.id'))
    state = db.relationship('state', foreign_keys=[state_id])

    def __init__(self, twitter, state=None, district=None):
        self.twitter = twitter

        # TODO: pull these details with tweepy to populate the data. may even do parsing on desc to get state/district
        self.name = None
        self.desc = None
        self.photo_url = None

        self.state = state
        self.district = district


db.create_all()
db.session.commit()
