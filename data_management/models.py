from sqlalchemy import Column, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from data_management.database import Base
import uuid


class Folder(Base):
    __tablename__ = "folders"
    __table_args__ = (
    UniqueConstraint("name", "parent_folder_id","owner_id"),
    )

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(String, nullable=False)

    parent_folder_id = Column(
        UUID(as_uuid=True),
        ForeignKey("folders.id"),
        nullable=True
    )

    owner_id = Column(UUID(as_uuid=True), nullable=False)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )