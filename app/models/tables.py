from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String, nullable=False)


    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)


class Data_Model(db.Model):
    __tablename__ = "data_model"

    id = db.Column(db.Integer, primary_key=True)
    input_data = db.Column(db.String, nullable=False)

    def __init__(self, input_data):
        self.input_data = input_data

class Model_Result(db.Model):
    __tablename__ = "model_result"

    id = db.Column(db.Integer, primary_key=True)
    model_result = db.Column(db.String, nullable=False)

    def __init__(self, model_result):
        self.model_result = model_result






