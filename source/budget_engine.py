from source.models import BudgetSummary, ContractTerms

def calculate_remaining_balance(total_budget: float, contracts: list[ContractTerms]) -> BudgetSummary:
    committed = sum(contract.total_amount for contract in contracts)
    remaining = total_budget - committed
    overrun = abs(remaining) if remaining < 0 else 0.0
    return BudgetSummary(total_budget=total_budget, committed_amount=committed, remaining_balance=max(remaining, 0.0), overrun_amount=overrun)
