import re

def detect_clauses(text):
    clauses = {
        "Termination": r"(termination.*?clause|terminate.*?agreement)",
        "Liability": r"(limited.*?liability|liability.*?excluded)",
        "Confidentiality": r"(confidential.*?information|non-disclosure)",
        "Indemnification": r"(indemnif(y|ication)|hold harmless)",
        "Dispute Resolution": r"(dispute.*?resolution|arbitration|governing law)",
        "Payment Terms": r"(payment terms|fees|invoicing)",
    }

    results = {}
    for name, pattern in clauses.items():
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            results[name] = matches
    return results
