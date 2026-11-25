"""Deterministic financial and budget calculation interface (non-AI code)."""

from source.models import BudgetSummary, ContractTerms


def calculate_remaining_balance(total_budget: float, contracts: list[ContractTerms]) -> BudgetSummary:
    """Calculate committed totals, remaining budget balance, and any overrun."""
    pass  