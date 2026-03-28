from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ComplaintCreate(BaseModel):
    citizen_name: Optional[str] = None
    description: str
    location: Optional[str] = None

class ComplaintResponse(BaseModel):
    id: int
    citizen_name: Optional[str]
    description: str
    category: Optional[str]
    severity: Optional[float]
    priority: Optional[str]
    department: Optional[str]
    status: str
    location: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True  

class AuditLogResponse(BaseModel):
    id: int
    complaint_id: int
    agent_name: str
    action: str
    input_data: Optional[dict]
    output_data: Optional[dict]
    status: str
    error_message: Optional[str]
    retry_count: int
    timestamp: datetime

    class Config:
        from_attributes = True 