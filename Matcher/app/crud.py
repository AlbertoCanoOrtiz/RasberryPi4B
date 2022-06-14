from sqlalchemy.orm import Session
import models, schemas


def get_adopter_( db: Session, skip: int = 0, limit: int = 0 ):
  db_adopter = db.query(models.Adopter).offset(skip).limit(limit).all()
  return db_adopter

def get_animal_( db: Session, skip: int  = 0, limit: int = 0 ):
  db_animal = db.query(models.Animal).offset(skip).limit(limit).all()
  return db_animal

def get_partnership(db: Session, skip: int=  0, limit: int = 0 ):
  db_partnership = db.query(models.Partnership).offset(skip).limit(limit).all()
  return db_partnership
  
def get_sociophat_( db: Session, skip: int = 0, limit: int= 0 ):
  db_sociophat = db.query(models.Sociophat).offset(skip).limit(limit).all()
  return db_sociophat
