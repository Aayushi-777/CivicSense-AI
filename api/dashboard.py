from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from core.models import Complaint
from fastapi import HTTPException

router = APIRouter()

@router.get("/dashboard")
def get_dashboard(db: Session = Depends(get_db)):
    complaints = db.query(Complaint).all()

    total = len(complaints)
    pending = len([c for c in complaints if c.status == "PENDING"])
    in_progress = len([c for c in complaints if c.status == "IN_PROGRESS"])
    resolved = len([c for c in complaints if c.status == "RESOLVED"])

    return {
        "total": total,
        "pending": pending,
        "in_progress": in_progress,
        "resolved": resolved,
        "complaints": [
            {
                "id": c.id,
                "description": c.description,
                "category": c.category,
                "priority": c.priority,
                "status": c.status
            } for c in complaints
        ]
    }
@router.delete("/complaint/{complaint_id}")
def delete_complaint(complaint_id: int, db: Session = Depends(get_db)):
    complaint = db.query(Complaint).filter(Complaint.id == complaint_id).first()

    if not complaint:
        raise HTTPException(status_code=404, detail="Complaint not found")

    db.delete(complaint)
    db.commit()

    return {"message": "Complaint deleted"}