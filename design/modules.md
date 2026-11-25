# Architecture & System Modules (`design/modules.md`)

## 1. Overview
This document defines the module architecture for `wedding-vendor-ai`, ensuring a clear separation between standard deterministic code (financial logic, tools) and AI-driven capabilities (multi-turn intake, contract parsing, draft outreach).

---

## 2. Module Specifications

### Module A: User Preference & Multi-Turn Intake (`intake_agent`)
- **Responsibility:** Manages multi-turn conversation loops with the couple to clarify preferences, constraints, and budget details until complete. Enforces structured JSON output without needing AI to parse the result.
- **Inputs:** Chat input from couple, context history.
- **Outputs:** Validated `PreferencesJSON` structure.
- **Implementation:** **AI/LLM-driven (Multi-turn Agent Loop)** with strict JSON schema outputs. Used in Scenario 1.

### Module B: Contract & Term Extractor (`contract_parser`)
- **Responsibility:** Extracts contract terms, required deposits, cancellation clauses, overtime fees, and venue rules from uploaded vendor documents.
- **Inputs:** PDF/Images/Text of vendor contracts.
- **Outputs:** Structured `ContractTermsJSON`.
- **Implementation:** **AI/LLM-driven (RAG / Extraction)**. Used in Scenario 1.

### Module C: Financial & Budget Engine (`budget_calculator`)
- **Responsibility:** Performs accurate budget tracking, remaining balance calculations, overrun alerts, payment due dates, and guest count financial impact.
- **Inputs:** `PreferencesJSON`, `ContractTermsJSON`, user budget limits.
- **Outputs:** Calculated budget breakdown, remaining balances, payment alerts.
- **Implementation:** **Standard Code (Pure Python - NON-AI)**. Guarantees 100% calculation accuracy. Used in Scenario 1.

### Module D: Tool Calling & Integration Hub (`tools_hub`)
- **Responsibility:** Executes standard code functions to update budget tables, set calendar reminders, and fetch vendor database entries.
- **Inputs:** Tool execution requests from system/agents.
- **Outputs:** Database status, updated files, scheduled reminders.
- **Implementation:** **Standard Code (Tool Calling)**. Used in Scenario 1.

### Module E: Vendor Outreach & Human Mediator (`outreach_mediator`)
- **Responsibility:** Generates vendor outreach drafts for venue availability/scheduling, but routes all outgoing messages through a Human Mediator (company representative) before sending.
- **Inputs:** Message parameters, vendor target details.
- **Outputs:** Approved dispatched outreach or revision request.
- **Implementation:** **Hybrid (AI Drafting + Human Mediator Guardrail Loop)**.

---

## 3. Data & Communication Flow (Scenario 1)
1. **Intake / Contract Input:** `contract_parser` (AI) extracts payment schedule -> outputs `ContractTermsJSON`.
2. **Financial Calculation:** `budget_calculator` (Code) updates the central budget and computes remaining balance.
3. **Execution & Calendar:** `tools_hub` (Code) updates the budget ledger and creates payment reminders.