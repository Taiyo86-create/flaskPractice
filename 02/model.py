import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column

base_dir = os.path.dirname(__file__)

app = Flask(__name__)

# データベース設定
database_path = os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'

Base = declarative_base()

db = SQLAlchemy(app, model_class=Base)

class Person(db.Model):
    __tablename__ = 'person'
    id = mapped_column(db.Integer, primary_key=True)
    name = mapped_column(db.String)
    age = mapped_column(db.Integer)
    
    def __str__(self):
        return f"id={self.id}, name={self.name}, age={self.age}"
    
print(db)
print(db.metadata.tables)
