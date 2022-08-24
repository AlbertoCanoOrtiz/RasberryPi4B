from sqlalchemy.orm import Session
import models, schemas
import json

def get_adopter_( db: Session, skip: int = 0, limit: int = 1000 ):
  db_adopter = db.query(schemas.Adopter).offset(skip).limit(limit).all()
  return db_adopter

def get_animal_( db: Session, breed : str, color: str, skip: int  = 0, limit: int = 1000 ):
  db_animal = db.query(schemas.Animal).offset(skip).limit(limit).all()
  db_animal = [it.__dict__ for it in db_animal].pop()
  del db_animal['_sa_instance_state']
  return db_animal

def get_partnership_(db: Session, skip: int=  0, limit: int = 1000 ):
  db_partnership = db.query(schemas.Partnership).offset(skip).limit(limit).all()
  db_partnership = [it.__dict__ for it in db_partnership].pop()
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


