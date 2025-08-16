from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import database
from schemas.users import UserModel, UserResponse
from models.users import Users
from datetime import datetime

app = FastAPI(title='Imtihon API', docs_url='/')

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
)

@app.post('/add')
def add_user(form: UserModel, db: Session = Depends(database)):
    user = Users(
        name = form.name,
        age = form.age,
        address = form.address,
        balans = 0,
        birth_date = datetime.now().year - form.age
    )
    db.add(user)
    db.commit()
    return {'message': 'User qoshildi !'}


@app.get('/get', response_model=List[UserResponse])
def get_user(db: Session = Depends(database)):
    return db.query(Users).all()


@app.put('/income')
def income_balans(ident:int, balans:int, db: Session = Depends(database)):
    db.query(Users).filter(Users.id == ident).update({
        Users.balans: Users.balans + balans
    })
    db.commit()
    return {'message': 'Foyda qoshildi !'}




