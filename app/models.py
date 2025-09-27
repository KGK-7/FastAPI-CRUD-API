from pydantic import BaseModel
from sqlalchemy import Table, Column, Integer, String
from app.database import metadata, engine

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("email", String, nullable=False)
)

# Create table in DB
metadata.create_all(engine)

class User(BaseModel):
    id: int
    name: str
    email: str
