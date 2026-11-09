"""Pydantic schemas for Risk Management domain."""

from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID

from backend.app.schemas.base import PMOBaseModel, TimestampMixin


class RiskCategory(str, Enum):
    """Risk category enumeration."""
    FINANCIAL = "financial"
    OPERATIONAL = "operational"
    STRATEGIC = "strategic"
    COMPLIANCE = "compliance"
    TECHNICAL = "technical"


class RiskSeverity(str, Enum):
    """Risk severity enumeration."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class RiskStatus(str, Enum):
    """Risk status enumeration."""
    OPEN = "open"
    MITIGATED = "mitigated"
    CLOSED = "closed"
    ESCALATED = "escalated"


class RiskBase(PMOBaseModel):
    """Base risk schema with common fields."""
    title: str
    description: Optional[str] = None
    category: RiskCategory
    severity: RiskSeverity
    status: RiskStatus
    mitigation_plan: Optional[str] = None
    owner_id: Optional[UUID] = None


class RiskCreate(RiskBase):
    """Schema for creating a new risk."""
    pass


class RiskUpdate(PMOBaseModel):
    """Schema for updating an existing risk (all fields optional)."""
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[RiskCategory] = None
    severity: Optional[RiskSeverity] = None
    status: Optional[RiskStatus] = None
    mitigation_plan: Optional[str] = None
    owner_id: Optional[UUID] = None


class RiskResponse(RiskBase, TimestampMixin):
    """Schema for risk response with full details."""
    id: UUID
    initiative_id: UUID


class RiskListResponse(PMOBaseModel):
    """Schema for paginated risk list response."""
    items: list[RiskResponse]
    total: int
    page: int
    page_size: int
    pages: int


class RiskFilterParams(PMOBaseModel):
    """Query parameters for filtering risks."""
    severity: Optional[RiskSeverity] = None
    status: Optional[RiskStatus] = None
    category: Optional[RiskCategory] = None
