"""SQLAlchemy model for Decision entity."""

import uuid
from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import Column, DateTime, Enum, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from backend.app.db.base import Base


class ApprovalBoundary(str, PyEnum):
    """Approval boundary enumeration."""
    EXECUTIVE = "executive"
    TEAM = "team"
    EXTERNAL = "external"


class DecisionStatus(str, PyEnum):
    """Decision status enumeration."""
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    DEFERRED = "deferred"


class Decision(Base):
    """Decision model for tracking initiative decisions."""
    
    __tablename__ = "decisions"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    initiative_id = Column(UUID(as_uuid=True), ForeignKey("initiatives.id"), nullable=False, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    approval_boundary = Column(Enum(ApprovalBoundary), nullable=False)
    status = Column(Enum(DecisionStatus), nullable=False, default=DecisionStatus.PENDING)
    outcome = Column(Text, nullable=True)
    rationale = Column(Text, nullable=True)
    requested_by_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    decided_by_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    requested_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    decided_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    
    # Relationships
    initiative = relationship("Initiative", back_populates="decisions")
    requested_by = relationship("User", foreign_keys=[requested_by_id], back_populates="requested_decisions")
    decided_by = relationship("User", foreign_keys=[decided_by_id], back_populates="decided_decisions")
