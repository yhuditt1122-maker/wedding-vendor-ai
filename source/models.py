"""Structured data types used across wedding-vendor-ai modules."""

from dataclasses import dataclass


@dataclass
class ContractTerms:
    """Structured terms extracted from a vendor contract."""

    vendor_name: str
    total_amount: float
    paid_amount: float
    next_due_date: str
    cancellation_policy: str


@dataclass
class BudgetSummary:
    """Calculated budget and remaining balance details."""

    total_budget: float
    committed_amount: float
    remaining_balance: float
    overrun_amount: float