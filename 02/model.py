import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column

base_dir = os.path.dirname(__file__)

app = Flask(__name__)

# データベース設定
database_path = os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URL'] = f'sqlite:///{database_path}'