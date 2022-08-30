from fastapi import HTTPException
from sqlalchemy.orm import Session
import models, schemas
import json

def get_adopter_(db: Session, rfc: str, gender: str, street: str, number: int , skip: int = 0, limit: int = 1000 ):

  if gender and street and number: 
    db_adopter = db.query(schemas.Adopter).filter(schemas.Adopter.rfc == rfc).filter(schemas.Adopter.gender == gender).filter(schemas.Adoptar.street == street).filter(schemas.Adopter.number == number ).offset(skip).limit(limit).first()
  elif gender:
    db_adopter = db.query(schemas.Adopter).filter(schemas.Adopter.rfc == rfc).filter(schemas.Adopter.gender == gender).offset(skip).limit(limit).first()
  elif street: 
    db_adopter = db.query(schemas.Adopter).filter(schemas.Adopter.rfc == rfc).filter(schemas.Adopter.street == street).offset(skip).limit(limit).first()
  else:
    db_adopter = db.query(schemas.Adopter).filter(schemas.Adopter.rfc == rfc).offset(skip).limit(limit).first()

  if db_adopter is None:
    raise HTTPException(status_code= 404, detail='NOT FOUND')

  db_adopter = db_adopter.__dict__
  del db_adopter['_sa_instance_state']
  
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
    db_partnership = db.query(schemas.Partnership).filter(schemas.Partnership.rfc == rfc).filter(schemas.Partnership.street == street).filter(schemas.Partnership.number == number).offset(skip).limit(limit).first()
  elif street:
    db_partnership = db.query(schemas.Partnership).filter(schemas.Partnership.rfc == rfc).filter(schemas.Partnership.street == street).offset(skip).limit(limit).first()
  elif number:
    db_partnership = db.query(schemas.Partnership).filter(schemas.Partnership.rfc == rfc).filter(schemas.Partnership.number == number).offset(skip).limit(limit).first()
  else :
    db_partnership = db.query(schema.Partnership).filter(schemas.Partnership.rfc == rfc).offset(skip).limit(limit).first()
    
  if db_partnership is None:
    raise HTTPException(status_code=404,detail='NOT FOUND')

  db_partnership = db_partnership.__dict__ 
  del db_partnership['_sa_instance_state']

  return db_partnership


def get_sociopath_( db: Session, gender: str, street: str, number: int, code: int, skip: int = 0, limit: int= 1000):

  db_sociopath = db.query(schema.Sociopath)

  for it in  [(schema.Sociopath.gender, gender), (schema.Sociopath.street, street), (schema.Sociopath.number, number), (schema.Sociopath.code, code)] :
    if it[1]  :
      db_sociopath = db_sociopath.filter(it[0]==it[1])

  db_sociopath = db_sociopath.offset(skip).limit(limit).first()

  if db_sociopath is None:
    raise HTTPException(status_code=404,detail='NOT FOUND')

  db_sociopath = db_sociopath.__dict__  
  del db_sociopath['_sa_instance_state']


  return db_sociopath


def post_adopter_(db : Session, adopter : schemas.Adopter ):
  adopter = schemas.adopter(rfc=Adopter.rfc, gender=Adopter.gender, street=Adopter.street, number=Adopter.number, section=Adopter.section, district=Adopter.district, village=Adopter.village, country=Adopter.country, code=Adopter.code, email=Adopter.email, telphone=Adopter.telphone , celphone=Adopter.celphone, firstImage=Adopter.firstImage, secondImage=Adopter.secondImage, thirdImage=Adopter.thirdImage, signDate=Adopter.signDate, statusInd=Adopter.statusInd)
  db.add(adopter)
  db.commit()
  db.refresh(adopter)
  return {'200' : 'This is a test only in the case of show in the screen; itwill be the way to pint codes' }

def post_animal_(db : Session, animal : schemas.Animal ):
  animal= schemas.Animal(size=animal.size, body=animal.body, chest=animal.chest, neck=animal.neck, breed=animal.breed, color=animal.color, firstImage=animal.firstImage, secondImage=animal.secondImage, thirdImage=animal.thirdImage, fourthImage=animal.fourthImage, fifthImage=animal.fifthImage, sixthImage=animal.sixthImage, seventhImage=animal.seventhImage, eighthImage=animal.eighthImage, ninthImage=animal.ninthImage, tenthImage=animal.tenthImage, signDate=animal.signDate, statusInd=animal.statusInd)
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

  sociopath = schemas.Sociopath(rfc=Sociopath.rfc, gender=Sociopath.gender, street=Sociopath.street, number=Sociopath.number, section=Sociopath.section, district=Sociopath.district, village=Sociopath.village, country=Sociopath.country, code=Sociopath.code, secondImage=Sociopath.secondImage, thirdImage=Sociopath.thirdImage, signDate=Sociopath.signDate, statusInd=Sociopath.statusInd)
  db.add(sociopath)
  db.commit()
  db.refresh()
  return {'200' : 'This is a test only in the case of show in the screen; itwill be the way to pint codes' }


def delete_animal_(db: Session, breed : str , color: str, skip: int  = 0, limit: int = 1000):
  db_animal = db.query(schemas.Animal) 
  for it in [(schemas.Animal.breed, breed.replace('%',' ')),(schemas.Animal.color, color.value)]:
    if it[1]:
      db_animal = db_animal.filter(it[0]==it[1])

  if db_animal.first() is None:
    raise HTTPException(status_code=404, detail='NOT FOUND')

  db_animal.delete()
  db.commit()
  return models.Success(code='200', message='this is a test in the case of show in the screen; it will be the way to print codes')

def delete_adopter_(db: Session, rfc: str, gender: str, street: str, number: int , skip: int = 0, limit: int = 1000 ):
  db_adopter = db.query(schemas.Adopter)  
  for it in [(schemas.Adopter.rfc, rfc), (schemas.Adopter.gender, gender), (schemas.Adopter.street.replace('%',' '), street), (schemas.Adopter.number, number)]:
    if it[1]:
      db_adopter = db_adopter.filter(it[0]==it[1])

  if db_adopter.first() is None:
    raise HTTPException(status_code=404, detail='NOT FOUND')
    
  db_adopter.delete()
  db.commit()
  return models.Success(code='200', message='this is a test in the case of show in the screen; it will be the way to print codes')


def delete_partnership_(db: Session, rfc: str, street: str, number: int, skip: int=  0, limit: int = 1000):
  db_partnership = db.query(schemas.Partnership)
  for it in [(schemas.Partnership.rfc, rfc), (schemas.Partnership.street.replace('%',' '), street), (schemas.Partnership.number, number)]:
    if it[1] :
      db_partnership = db_partnership.filter(it[0]==it[1])

  if db_partnership.first() is None:
    raise HTTPException(status_code=404, detail = 'NOT FOUND')
    
  db_partnership.delete()
  db.commit()
  return models.Success(code='200', message='this is a test in the case of show in the screen; it will be the way to print codes')


def delete_sociopath_(db: Session, rfc: str, gender: str, street: str, number: int, code: int, skip: int = 0, limit: int= 1000):
  db_sociopath = db.query(schemas.Sociopath)
  for it in  [(schemas.Sociopath.rfc, rfc), (schemas.Sociopath.gender, gender), (schemas.Sociopath.street, street.replace('%',' ')), (schemas.Sociopath.number, number), (schemas.Sociopath.code, code)]:
    if it[1]:
      db_sociopath = db_sociopath.filter(it[0]==it[1])

  if db_sociopath.first() is None:
    raise HTTPException(status_code=404, detail='NOT FOUND')
  
  db_sociopath.delete()
  db.commit()
  return models.Success(code='200' ,  message='This is a test only in the case of show in the screen; it will be the way to pint codes' )


def update_animal_(db: Session, breed : str , color: str, skip: int  = 0, limit: int = 1000):
  db_animal = db.query(schemas.Animal)
  for it in [(schemas.Animal.breed, breed.replace('%',' ')),(schemas.Animal.color, color.value),(schemas.Animal.statusInd,True)]:
    if it[1]:
      db_animal = db_animal.filter(it[0]==it[1])

  if db_animal.first() is None:
    message = post_animal()
  else: 
    db_animal.
    db_animal.delete()

  db.commit()
  return models.Success(code='200', message='this is a test in the case of show in the screen; it will be the way to print codes')


def update_adopter_(db: Session, rfc: str, gender: str, street: str, number: int , skip: int = 0, limit: int = 1000):
  db_adopter = db.query(schemas.Adopter)
  for it in [(schemas.Adopter.rfc, rfc), (schemas.Adopter.gender, gender), (schemas.Adopter.street.replace('%',' '), street), (schemas.Adopter.number, number)]:
    if it[1]:
      db_adopter = db_adopter.filter(it[0]==it[1])

  if db_adopter.first() is None:
    ...
  else :
    ...
    db_adopter.delete()
  db.commit()
  return models.Success(code='200', message='this is a test in the case of show in the screen; it will be the way to print codes')

def update_partnership_(db: Session, rfc: str, street: str, number: int, skip: int=  0, limit: int = 1000):
  db_partnership = db.query(schemas.Partnership)
  for it in [(schemas.Partnership.rfc, rfc), (schemas.Partnership.street.replace('%',' '), street), (schemas.Partnership.number, number)]:
    if it[1] :
      db_partnership = db_partnership.filter(it[0]==it[1])

  if db_partnership.first() is None:
    ...
  else:
    ...
    db_partnership.delete()
  db.commit()
  return models.Success(code='200', message='this is a test in the case of show in the screen; it will be the way to print codes')


def update_sociopath_(db: Session, rfc: str, gender: str, street: str, number: int, code: int, skip: int = 0, limit: int= 1000):
  db_sociopath = db.query(schemas.Sociopath)
  for it in  [(schemas.Sociopath.rfc, rfc), (schemas.Sociopath.gender, gender), (schemas.Sociopath.street, street.replace('%',' ')), (schemas.Sociopath.number, number), (schemas.Sociopath.code, code)]:
    if it[1]:
      db_sociopath = db_sociopath.filter(it[0]==it[1])

  if db_sociopath.first() is None:
    ...
  else:
    ...
    db_sociopath.delete()
  db.commit()
  return models.Success(code='200' ,  message='This is a test only in the case of show in the screen; it will be the way to pint codes' )

