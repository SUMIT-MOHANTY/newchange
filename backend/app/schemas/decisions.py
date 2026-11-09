"""Pydantic schemas for Decision Tracking domain."""

from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID

from backend.app.schemas.base import PMOBaseModel, TimestampMixin


class ApprovalBoundary(str, Enum):
    """Approval boundary enumeration."""
    EXECUTIVE = "executive"
    TEAM = "team"
    EXTERNAL = "external"


class DecisionStatus(str, Enum):
    """Decision status enumeration."""
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    DEFERRED = "deferred"


class DecisionBase(PMOBaseModel):
    """Base decision schema with common fields."""
    title: str
    description: Optional[str] = None
    approval_boundary: ApprovalBoundary
    status: DecisionStatus
    outcome: Optional[str] = None
    rationale: Optional[str] = None
    requested_by_id: Optional[UUID] = None
    decided_by_id: Optional[UUID] = None
    requested_at: Optional[datetime] = None
    decided_at: Optional[datetime] = None


class DecisionCreate(PMOBaseModel):
    """Schema for creating a new decision request."""
    title: str
    description: Optional[str] = None
    approval_boundary: ApprovalBoundary
    requested_by_id: Optional[UUID] = None


class DecisionUpdate(PMOBaseModel):
    """Schema for updating an existing decision (all fields optional)."""
    title: Optional[str] = None
    description: Optional[str] = None
    approval_boundary: Optional[ApprovalBoundary] = None
    status: Optional[DecisionStatus] = None
    outcome: Optional[str] = None
    rationale: Optional[str] = None
    decided_by_id: Optional[UUID] = None
    decided_at: Optional[datetime] = None


class DecisionResponse(DecisionBase, TimestampMixin):
    """Schema for decision response with full details."""
    id: UUID
    initiative_id: UUID
    turnaround_hours: Optional[float] = None


class DecisionListResponse(PMOBaseModel):
    """Schema for paginated decision list response."""
    items: list[DecisionResponse]
    total: int
    page: int
    page_size: int
    pages: int


class DecisionFilterParams(PMOBaseModel):
    """Query parameters for filtering decisions."""
    status: Optional[DecisionStatus] = None
    approval_boundary: Optional[ApprovalBoundary] = None
