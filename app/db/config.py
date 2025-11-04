from sqlmodel import SQLModel, create_engine,Session
import os
from typing import Annotated
from fastapi import Depends

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

db_path = os.path.join(BASE_DIR,"vicky.db")

DATABASE_URL = f"sqlite:///{db_path}"

engine = create_engine(DATABASE_URL, echo=True)

def create_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield

sessionDep = Annotated[Session, Depends(get_session)]