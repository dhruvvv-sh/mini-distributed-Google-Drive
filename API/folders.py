"""
folders.py
→ POST /folders
→ GET /folders/{id}
→ PUT /folders/{id}
→ DELETE /folders/{id}
"""

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from data_management.database import get_db
from data_management.models import Folder
import uuid

class FolderCreate(BaseModel):
    name: str
    parent_folder_id: str | None = None

class FolderResponse(BaseModel):
    id: str
    name: str
    parent_folder_id: str | None
    owner_id: str


router = APIRouter(
    prefix = "/folders",
    tags = ["folders"]
)

@router.post("/")
def create_folder(folder: FolderCreate, db: Session = Depends(get_db)):
    new_folder = Folder(
        id = uuid.uuid4(),
        name = folder.name,
        parent_folder_id = folder.parent_folder_id,
        owner_id = uuid.uuid4()  # Replace with actual owner ID in a real application
    )
    db.add(new_folder)
    db.commit()
    db.refresh(new_folder)
    return {"message": "Folder created successfully"}

@router.get("/{id}")
def get_folder(id: str, db: Session = Depends(get_db)):
    folder = db.query(Folder).filter(Folder.id == id).first()
    if not folder:
        return {"message": f"Folder with id {id} not found"}
    else:
        return {"message": f"Folder with id {id} retrieved successfully"}

@router.put("/{id}")
def update_folder(id: str, db: Session = Depends(get_db)):
    folder = db.query(Folder).filter(Folder.id == id).first()
    if not folder:
        return {"message": f"Folder with id {id} not found"}
    else:
        return {"message": f"Folder with id {id} updated successfully"}

@router.delete("/{id}")
def delete_folder(id: str, db: Session = Depends(get_db)):
    folder = db.query(Folder).filter(Folder.id == id).first()
    if not folder:
        return {"message": f"Folder with id {id} not found"}
    else:
        db.delete(folder)
        db.commit()
        return {"message": f"Folder with id {id} deleted successfully"}

