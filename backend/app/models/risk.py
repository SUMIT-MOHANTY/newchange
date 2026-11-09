"""SQLAlchemy model for Risk entity."""

import uuid
from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import Column, DateTime, Enum, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from backend.app.db.base import Base


class RiskCategory(str, PyEnum):
    """Risk category enumeration."""
    FINANCIAL = "financial"
    OPERATIONAL = "operational"
    STRATEGIC = "strategic"
    COMPLIANCE = "compliance"
    TECHNICAL = "technical"


class RiskSeverity(str, PyEnum):
    """Risk severity enumeration."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class RiskStatus(str, PyEnum):
    """Risk status enumeration."""
    OPEN = "open"
    MITIGATED = "mitigated"
    CLOSED = "closed"
    ESCALATED = "escalated"


class Risk(Base):
    """Risk model for tracking project risks."""
    
    __tablename__ = "risks"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    initiative_id = Column(UUID(as_uuid=True), ForeignKey("initiatives.id"), nullable=False, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    category = Column(Enum(RiskCategory), nullable=False)
    severity = Column(Enum(RiskSeverity), nullable=False)
    status = Column(Enum(RiskStatus), nullable=False, default=RiskStatus.OPEN)
    mitigation_plan = Column(Text, nullable=True)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    
    # Relationships
    initiative = relationship("Initiative", back_populates="risks")
    owner = relationship("User", back_populates="owned_risks")
