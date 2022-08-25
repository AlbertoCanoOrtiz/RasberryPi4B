from fastapi import HTTPException
from sqlalchemy.orm import Session
import models, schemas
import json

def get_adopter_(db: Session, rfc: str, gender str, street: str, number: int , skip: int = 0, limit: int = 1000 ):
  db_adopter = db.query(schemas.Adopter).offset(skip).limit(limit).all()
  return db_adopter

def get_animal_( db: Session, breed : str , color: str, skip: int  = 0, limit: int = 1000 ):

  if breed and color:
    db_animal = db.query(schemas.Animal).filter(schemas.Animal.color == color.value).filter(schemas.Animal.breed == breed.upper().replace('%',' ')).offset(skip).limit(limit).first()
  elif breed: 
    db_animal = db.query(schemas.Animal).filter(schemas.Animal.breed == breed.upper().replace('%',' ')).offset(skip).limit(limit).first()
  elif color: 
    db_animal = db.query(schemas.Animal).filter(schemas.Animal.color == color.value).offset(skip).limit(limit).first()
  else :
    db_animal = db.query(schemas.Animal).offset(skip).limit(limit).first()

  if db_animal is None:
    raise HTTPException(status_code=404,detail='NOT FOUND')
  
  db_animal = db_animal.__dict__
  del db_animal['_sa_instance_state']

  return db_animal


def get_partnership_(db: Session, rfc: str, street: str, number: int, skip: int=  0, limit: int = 1000 ):

  if street and number:
    db_partnership = db.query(schemas.Partnership).filter(schemas.Partnership.rfc = rfc).filter(schemas.Partnership.street = street).filter(schemas.Partnership.number = number).offset(skip).limit(limit).first()
  elif street:
    db_partnership = db.query(schemas.Partnership).filter(schemas.Partnership.rfc = rfc).filter(schemas.Partnership.street= street).offset(skip).limit(limit).first()
  elif number:
    db_partnership = db.query(schemas.Partnership).filter(schemas.Partnership.rfc = rfc).filter(schemas.Partnership.number = number).offset(skip).limit(limit).first()
  else :
    db_partnership = db.query(schema.Partnership).filter(schemas.Partnership.rfc = rfc).offset(skip).limit(limit).first()
    
  db_partnership = it.__dict__ 
  del db_partnership['_sa_instance_state']

  return db_partnership


def get_sociopath_( db: Session, skip: int = 0, limit: int= 1000 ):
  db_sociopath = db.query(schemas.Sociophat).offset(skip).limit(limit).all()
  db_sociopath = [it.__dict__ for it in db_sociopath].pop()
  del db_sociopath['_sa_instance_state']
  return db_sociopath

def post_adopter_(db : Session, adopter : schemas.Adopter ):
  db.add(adopter)
  db.commit()
  db.refresh(adopter)
  return {'200' : 'This is a test only in the case of show in the screen; itwill be the way to pint codes' }

def post_animal_(db : Session, animal  : schemas.Animal ):
  animal= 
  
  db.add(animal)
  db.commit()
  db.refresh(animal)
  return {'200' : 'This is a test only in the case of show in the screen; itwill be the way to pint codes' }


def post_partnership_(db : Session, partnership : schemas.Partnership ):
  partnership = schemas.Partnership(rfc=partnership.rfc, street=partnership.street, number=partnership.number, section=partnership.section, district=partnership.district, village=partnership.village, country=partnership.country, code=partnership.code, email=partnership.email, telephone=partnership.telephone, celphone=partnership.celphone, url=partnership.url, firstImage=partnership.firstImage,secondImage=partnership.secondImage, thirdImage=partnership.thirdImage,signDate=partnership.signDate, statusInd=partnership.statusInd)
  db.add(partnership)
  db.commit()
  db.refresh(partnership)
  return {'200' : 'This is a test only in the case of show in the screen; itwill be the way to pint codes' }

def post_sociopath_(db : Session, sociopath : schemas.Sociopath ):
  db.add(sociopath)
  db.commit()
  db.refresh()
  return {'200' : 'This is a test only in the case of show in the screen; itwill be the way to pint codes' }


def delete_sociopath_(db: Session, rfc: str):
  db.query(schemas.Sociopath).filter(schemas.Sociopath.rfc == rfc).delete()
  db.commit()
  return models.Success(code='200' ,  message='This is a test only in the case of show in the screen; itwill be the way to pint codes' )


