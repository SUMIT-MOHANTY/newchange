"""Pure business logic functions for Benefits Realization domain.

This module contains stateless, unit-testable computation functions
for variance percentage and turnaround hours calculations.
"""

from datetime import datetime


def compute_variance_percentage(planned: float, actual: float) -> float:
    """Compute variance percentage between planned and actual values.
    
    Formula: ((actual - planned) / planned) * 100
    
    Args:
        planned: The planned/target value.
        actual: The actual achieved value.
        
    Returns:
        Variance percentage rounded to 2 decimal places.
        Returns 0.0 if planned is zero (division by zero guard).
    """
    if planned == 0:
        return 0.0
    variance = ((actual - planned) / planned) * 100
    return round(variance, 2)


def compute_turnaround_hours(requested_at: datetime, decided_at: datetime) -> float:
    """Compute turnaround time in hours between request and decision.
    
    Args:
        requested_at: Timestamp when the decision was requested.
        decided_at: Timestamp when the decision was made.
        
    Returns:
        Turnaround time in decimal hours rounded to 1 decimal place.
        
    Raises:
        ValueError: If decided_at is earlier than requested_at.
    """
    if decided_at < requested_at:
        raise ValueError("decided_at cannot be earlier than requested_at")
    
    delta = decided_at - requested_at
    hours = delta.total_seconds() / 3600
    return round(hours, 1)
