from sqlalchemy import Column, DateTime, Integer, String
from datetime import datetime

from database.database import Base
from enums.users import Country, Enum, Acct_type


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(300))
    last_name = Column(String(300))
    country = Column(Enum(Country))
    email = Column(String, unique=True, index=True)
    password = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True),
                        nullable=False, default=datetime.now())
    updated_at = Column(DateTime(timezone=True),
                        nullable=False, default=datetime.now())
    acct_type = Column(Enum(Acct_type))

