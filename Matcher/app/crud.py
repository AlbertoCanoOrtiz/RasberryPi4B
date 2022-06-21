from sqlalchemy.orm import Session
import models, schemas


def get_adopter_( db: Session, skip: int = 0, limit: int = 0 ):
  db_adopter = db.query(schemas.Adopter).offset(skip).limit(limit).all()
  return db_adopter

def get_animal_( db: Session, skip: int  = 0, limit: int = 0 ):
  db_animal = db.query(schemas.Animal).offset(skip).limit(limit).all()
  return db_animal

def get_partnership_(db: Session, skip: int=  0, limit: int = 0 ):
  db_partnership = db.query(schemas.Partnership).offset(skip).limit(limit).all()
  return db_partnership
  
def get_sociopath_( db: Session, skip: int = 0, limit: int= 0 ):
  db_sociopath = db.query(schemas.Sociophat).offset(skip).limit(limit).all()
  return db_sociopath
