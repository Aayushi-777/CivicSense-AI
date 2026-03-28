from sqlalchemy import Column, Integer, String, Float

from core.database import Base

class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    category = Column(String)
    severity = Column(Float)
    priority = Column(String)
    department = Column(String)
    status = Column(String, default="PENDING")