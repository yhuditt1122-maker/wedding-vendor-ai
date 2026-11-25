"""Interface for extracting structured terms from vendor contracts."""

from source.models import ContractTerms


def extract_contract_terms(contract_text: str) -> ContractTerms:
    """Extract key financial and contract terms from raw contract text."""
    pass