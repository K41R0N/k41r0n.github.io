"""Generic boundary checks for accidentally retained client-specific details."""
import re

CLIENT_NAME_SENTINEL = "CLIENT_NAME_SENTINEL"
CLIENT_PERSON_SENTINEL = "CLIENT_PERSON_SENTINEL"
CLIENT_LEGAL_SENTINEL = "CLIENT_LEGAL_SENTINEL"

def check(text):
    found = []
    if CLIENT_NAME_SENTINEL in text:
        found.append(("fail", "R1-client-name", "Contains a synthetic client-name sentinel."))
    if CLIENT_PERSON_SENTINEL in text or CLIENT_LEGAL_SENTINEL in text:
        found.append(("fail", "R2-client-detail", "Contains a synthetic person/legal-detail sentinel."))
    if re.search(r"https?://|\b20\d\d-\d\d-\d\d\b", text, re.IGNORECASE):
        found.append(("fail", "R3-specific-reference", "Contains a raw URL or ISO date that needs review."))
    return found
