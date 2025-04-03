#  ____________________
#  Import LIBRARIES
from sqlmodel import SQLModel, create_engine
#  Import FILE
from . import models
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
