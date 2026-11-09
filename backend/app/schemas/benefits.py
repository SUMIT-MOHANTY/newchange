"""Pydantic schemas for Benefits Realization domain."""

from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID

from backend.app.schemas.base import PMOBaseModel, TimestampMixin


class BenefitCategory(str, Enum):
    """Benefit category enumeration."""
    COST_REDUCTION = "cost_reduction"
    REVENUE_GROWTH = "revenue_growth"
    EFFICIENCY_GAIN = "efficiency_gain"
    RISK_REDUCTION = "risk_reduction"
    COMPLIANCE = "compliance"


class BenefitStatus(str, Enum):
    """Benefit status enumeration."""
    ON_TRACK = "on_track"
    AT_RISK = "at_risk"
    ACHIEVED = "achieved"
    MISSED = "missed"


class BenefitBase(PMOBaseModel):
    """Base benefit schema with common fields."""
    category: BenefitCategory
    description: str
    planned_value: float
    actual_value: Optional[float] = None
    period: str
    unit: str
    status: BenefitStatus


class BenefitCreate(BenefitBase):
    """Schema for creating a new benefit record."""
    pass


class BenefitUpdate(PMOBaseModel):
    """Schema for updating an existing benefit (all fields optional)."""
    category: Optional[BenefitCategory] = None
    description: Optional[str] = None
    planned_value: Optional[float] = None
    actual_value: Optional[float] = None
    period: Optional[str] = None
    unit: Optional[str] = None
    status: Optional[BenefitStatus] = None


class BenefitResponse(BenefitBase, TimestampMixin):
    """Schema for benefit response with full details."""
    id: UUID
    initiative_id: UUID
    variance_percentage: Optional[float] = None


class BenefitListResponse(PMOBaseModel):
    """Schema for paginated benefit list response."""
    items: list[BenefitResponse]
    total: int
    page: int
    page_size: int
    pages: int


class BenefitFilterParams(PMOBaseModel):
    """Query parameters for filtering benefits."""
    status: Optional[BenefitStatus] = None
    category: Optional[BenefitCategory] = None
