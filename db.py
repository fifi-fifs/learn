#  ____________________
#  Import LIBRARIES
from sqlmodel import create_engine
#  Import FILE
from . import models
#  ____________________




sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)