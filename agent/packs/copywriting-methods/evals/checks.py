"""Small boundary checks for the generalized method reference."""
import re

def check(text):
    found=[]
    if re.search(r'\bSky(?:\.money|eco)?\b|sky\.money', text, re.I):
        found.append(('fail','R1-client-name','Contains an unredacted client brand name.'))
    if re.search(r'https?://|\b(?:Aymeric|Rune|Cahill|Howey|Forman)\b|\b20\d\d-\d\d-\d\d\b', text, re.I):
        found.append(('fail','R2-client-detail','Contains a likely client-specific link, identity, legal reference, or date.'))
    if re.search(r'\b(?:approved|safe|compliant) under (?:the )?(?:SEC|GENIUS Act|Howey|Forman)', text, re.I):
        found.append(('fail','R3-legal-claim','Contains a client-specific legal conclusion.'))
    return found
