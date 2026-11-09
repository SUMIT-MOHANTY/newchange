"""SQLAlchemy model for Benefit entity."""

import uuid
from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from backend.app.db.base import Base


class BenefitCategory(str, PyEnum):
    """Benefit category enumeration."""
    COST_REDUCTION = "cost_reduction"
    REVENUE_GROWTH = "revenue_growth"
    EFFICIENCY_GAIN = "efficiency_gain"
    RISK_REDUCTION = "risk_reduction"
    COMPLIANCE = "compliance"


class BenefitStatus(str, PyEnum):
    """Benefit status enumeration."""
    ON_TRACK = "on_track"
    AT_RISK = "at_risk"
    ACHIEVED = "achieved"
    MISSED = "missed"


class Benefit(Base):
    """Benefit model for tracking initiative benefits realization."""
    
    __tablename__ = "benefits"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    initiative_id = Column(UUID(as_uuid=True), ForeignKey("initiatives.id"), nullable=False, index=True)
    category = Column(Enum(BenefitCategory), nullable=False)
    description = Column(Text, nullable=False)
    planned_value = Column(Float, nullable=False)
    actual_value = Column(Float, nullable=True)
    period = Column(String(50), nullable=False)
    unit = Column(String(20), nullable=False)
    status = Column(Enum(BenefitStatus), nullable=False, default=BenefitStatus.ON_TRACK)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    
    # Relationships
    initiative = relationship("Initiative", back_populates="benefits")
