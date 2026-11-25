from source.budget_engine import calculate_remaining_balance
from source.contract_parser import extract_contract_terms

def run_scenario_1() -> None:
    raw_budget = input('Enter total wedding budget (or press Enter to exit): ').strip()
    if not raw_budget:
        return
    total_budget = float(raw_budget)
    contract_text = input('Paste vendor contract details: ').strip()
    contract = extract_contract_terms(contract_text)
    summary = calculate_remaining_balance(total_budget, [contract])
    print(f'Vendor: {contract.vendor_name} | Total contract: {contract.total_amount}')
    print(f'Remaining budget: {summary.remaining_balance} | Overrun: {summary.overrun_amount}')

if __name__ == '__main__':
    run_scenario_1()
