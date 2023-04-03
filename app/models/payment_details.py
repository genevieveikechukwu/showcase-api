from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from datetime import datetime
from database.database import Base


class Payment_detail(Base):
    __tablename__ = "payment_details"
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String(100))
    user_id = Column(Integer, ForeignKey("user.id")) 
    created_at = Column(DateTime(timezone=True),
                        nullable=False, default=datetime.now())
    updated_at = Column(DateTime(timezone=True),
                        nullable=False, default=datetime.now())
