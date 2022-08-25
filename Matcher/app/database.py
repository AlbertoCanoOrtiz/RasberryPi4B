from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

#os.getenv('POSTGRES_PASSWORD','postgres')
#os.getenv('POSTGRES_USER','postgres')
#os.getenv('POSTGRES_HOST', 'localhost')
#os.getenv('POSTGRES_DATABASE','postgres')


SQLALCHEMY_DATABASE_URL = 'postgresql://' + os.getenv('POSTGRES_USER','admin')  + ':'  +  os.getenv('POSTGRES_PASSWORD','hola-123') + '@' + os.getenv('POSTGRES_HOST','172.17.0.2') \
  + '/' + os.getenv('POSTGRES_DATABASE', 'opematraw') 

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.schema = os.getenv('POSTGRES_SCHEMA','matcher')
