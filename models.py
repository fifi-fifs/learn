#  ____________________
#  Import LIBRARIES
from sqlmodel import Field, SQLModel
#  Import FILES
#  ____________________



class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None
