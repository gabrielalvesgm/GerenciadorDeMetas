#models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    metas = db.relationship('Meta', backref='user', lazy=True)
    
class Meta(db.Model):
    __tablename__ = 'metas'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.String(500), nullable=True)
    prazo = db.Column(db.DateTime, nullable=False)
    prioridade = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='Pendente')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
