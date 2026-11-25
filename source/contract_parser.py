"""Stub implementation for extracting structured terms from vendor contracts."""

from source.models import ContractTerms


def extract_contract_terms(contract_text: str) -> ContractTerms:
    """Stub returning sample structured contract terms for Scenario 1."""
    return ContractTerms(
        vendor_name="Sample Wedding Vendor",
        total_amount=15000.0,
        paid_amount=5000.0,
        next_due_date="2027-01-15",
        cancellation_policy="30 days notice",
    )