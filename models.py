from app import db
from datetime import datetime


class Assignment(db.Model):
    __tablename__ = 'assignment'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    type = db.Column(db.String(50), nullable=False)  # e.g., 'online', 'offline'

    def __repr__(self):
        return f'<Assignment {self.title}>'


class Material(db.Model):
    __tablename__ = 'material'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # e.g., 'document', 'video'
    content = db.Column(db.Text, nullable=False)  # URL or text content

    def __repr__(self):
        return f'<Material {self.title}>'

