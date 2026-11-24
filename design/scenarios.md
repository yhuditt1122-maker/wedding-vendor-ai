\# Scenarios



\## 1. Calculate remaining balance and extract vendor contract terms



User: Couple planning the wedding (Yehudit and Shilav).

Trigger: The couple pastes a vendor quote or contract summary and enters the amount already paid.

Steps:

1\. Paste the vendor contract/quote text and enter the paid amount.

2\. Compute the remaining balance deterministically and extract key contract terms (total price, payment due dates, cancellation policy).

3\. Display the remaining balance and key terms to the couple.

Result: The couple sees the exact remaining balance to pay and a summary of the main contract terms.



Examples:

\- Input: "Photographer: 12000 NIS total. 3000 NIS deposit, balance due 14 days before event. Free cancellation up to 60 days prior." | Paid: 3000 NIS

&#x20; Expected remaining balance: 9000 NIS | Key terms: Total 12000 NIS, balance due 14 days before event, free cancellation up to 60 days prior.

\- Input: "DJ: 8500 NIS total. 2500 NIS paid today. Balance due on wedding day." | Paid: 2500 NIS

&#x20; Expected remaining balance: 6000 NIS | Key terms: Total 8500 NIS, balance due on wedding day.

\- Input: "Makeup and hair: 4200 NIS total. 1200 NIS paid, 3000 NIS due 30 days before." | Paid: 1200 NIS

&#x20; Expected remaining balance: 3000 NIS | Key terms: Total 4200 NIS, 3000 NIS due 30 days before.

