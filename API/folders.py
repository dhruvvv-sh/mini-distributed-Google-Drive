"""
folders.py
→ POST /folders
→ GET /folders/{id}
→ PUT /folders/{id}
→ DELETE /folders/{id}
"""

from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix = "/folders",
    tags = ["folders"]
)

@router.post("/")
def create_folder():
    return {"message": "Folder created successfully"}

@router.get("/{id}")
def get_folder(id: int):
    return {"message": f"Folder with id {id} retrieved successfully"}

@router.put("/{id}")
def update_folder(id: int):
    return {"message": f"Folder with id {id} updated successfully"}

@router.delete("/{id}")
def delete_folder(id: int):
    return {"message": f"Folder with id {id} deleted successfully"}

