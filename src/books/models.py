from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
import uuid


class Book(SQLModel, table=True):
    __tablename__ = "books"
    uid: uuid.UUID = Field(sa_column=Column(pg.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    title: str
    author: str
    category: str
    published_date: datetime = Field(default_factory=datetime.now())
    created_at : datetime = Field(default_factory=datetime.now())
    updated_at : datetime = Field(default_factory=datetime.now())


    def __repr__(self):
        return f"<Book(title={self.title})>"
