"""Base Pydantic schemas for the DERTOUR Portfolio Control Tower."""

from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class PMOBaseModel(BaseModel):
    """Base model for all PMO API schemas.
    
    Provides common configuration:
    - from_attributes: Enable ORM mode for SQLAlchemy model conversion
    - populate_by_name: Allow population by field name
    - str_strip_whitespace: Strip whitespace from string fields
    """
    
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        str_strip_whitespace=True,
    )


class TimestampMixin(BaseModel):
    """Mixin for timestamp fields."""
    
    created_at: datetime
    updated_at: datetime


class AuditLogEntry(PMOBaseModel):
    """Schema for audit log entries."""
    
    id: UUID
    entity_type: str
    entity_id: UUID
    action: str
    previous_state: dict[str, Any] | None = None
    new_state: dict[str, Any] | None = None
    performed_by_id: UUID | None = None
    performed_at: datetime


class PaginatedResponse(PMOBaseModel):
    """Base schema for paginated responses."""
    
    items: list[Any]
    total: int
    page: int
    page_size: int
    pages: int
