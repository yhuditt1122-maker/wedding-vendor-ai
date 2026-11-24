\# Wedding Vendor, Contract, and Budget AI Assistant: MVP



Pain: Couples planning a wedding are overwhelmed by dozens of complex vendor contracts (photographers, DJs, catering, designers, venues). Tracking fine print (overtime fees, cancellation terms, venue restrictions) and manually managing payment dates, guest counts, and budget leads to costly overruns and high stress.



Product: An AI assistant managing vendor communication and tracking contracts and budget end-to-end. The couple uploads contracts or chats with the AI; the system extracts key clauses, calculates payment balances and schedule, and manages vendor outreach for confirmations and missing details.



| Product Capability | Technique / System Component |

| --- | --- |

| Search vendors by natural-language preferences | RAG (retrieving information from contract documents) |

| Clarify preferences and constraints with the couple (interactive chat on budget or event style) | Multi-turn conversation + agent loop deciding whether to ask a follow-up question for complete info; structured output (no AI needed to parse structured output) |

| Manage exact budget calculations, remaining balances, overrun percentages, and guest count | Ordinary code (not AI) |

| Fetch vendor data, update central budget table, and set calendar reminders | Tool calling (ordinary code) |

| Reach out to vendors (email/message) for arrival confirmations, wedding-day schedule, and analyze replies | Multi-turn conversation, agent loop, tool calling; in the first outreach stage via message, include a human mediator from the company who contacts vendors and conducts the dialogue |

