#  ____________________
#  Import LIBRARIES
from sqlalchemy import Engine
from sqlmodel import SQLModel, create_engine
#  Import FILE
import models
# from .db import engine
#  ____________________




# Local DB
sqlite_file_name:str = "database.db"
sqlite_url:str= f"sqlite:///{sqlite_file_name}"
# In-memory DB
# sqlite_file_name:str = ""
# sqlite_url:str= f"sqlite://{sqlite_file_name}"

engine: Engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()