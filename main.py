from fastapi import (FastAPI, Depends, 
                     HTTPException,
                     status)
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from database import SessionLocal, engine
import schemas, crud, models
from sqlalchemy.orm import Session
import bcrypt
from typing import Annotated
# from security import get_current_user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)],
                     db: Annotated[Session, Depends(get_db)]):
    user = crud.get_user_by_email(db=db, email=token)
    return user
@app.get("/")
def home():
    return {"Hello" : "World"}


@app.post("/token")
async def oauth2_login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                       db: Annotated[Session, Depends(get_db)]):
    print(form_data)
    user_dict = crud.get_user_by_email(db=db, email=form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    if bcrypt.checkpw(password=form_data.password.encode("utf-8"),
                      hashed_password=user_dict.password.encode("utf-8")):
        return {"access_token": user_dict.email, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Incorrect username or password")


@app.post("/api/v1/register", response_model=schemas.User)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered!")
    return crud.create_user(db, user=user)

@app.get("/api/v1/users/me")
async def read_users_me(current_user: Annotated[schemas.User, Depends(get_current_user)]):
    return current_user



