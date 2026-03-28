from fastapi import APIRouter, Depends, Form, UploadFile, File
from sqlalchemy.orm import Session
import shutil
import os

from core.database import get_db
from core.models import Complaint
from agents.orchestrator import process_complaint

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/complaints")
def create_complaint(
    description: str = Form(...),
    file: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    image_path = None

    if file:
        image_path = f"{UPLOAD_DIR}/{file.filename}"
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    complaint = Complaint(description=description)
    db.add(complaint)
    db.commit()
    db.refresh(complaint)

    result = process_complaint(complaint.id, description, image_path, db)

    complaint.category = result["category"]
    complaint.priority = result["priority"]
    complaint.status = "IN_PROGRESS"

    db.commit()
    
    return {
    "id": complaint.id,
    "category": complaint.category,
    "priority": complaint.priority,
    "status": complaint.status
}  