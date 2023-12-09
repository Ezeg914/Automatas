# validators.py
import re, requests


def validate(data, regex):
    """Custom Validator"""
    return True if re.match(regex, data) else False


def validate_date(date: str):
    """Date Validator"""
    # Explicacion de la regex: https://regex101.com/r/CcpmFp/2
    reg = r"^(0[1-9]|[1|2][0-9]|3[0|1])+[\/]+(0[1-9]|1[0|1|2])+[\/]+(19|20)\d\d+\s+([01]\d|2[0-3]):([0-5]\d)$"
    return validate(date, reg)

def validate_user_id(user_id: str):
    """User ID Validator"""
    reg = r"^([\w\d]){16}$"
    return validate(user_id, reg)

def validate_mac_ap(mac_ap: str):
    """MAC AP Validator"""
    reg = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}):UM$"
    return validate(mac_ap, reg)

def validate_mac(mac: str):
    """MAC Validator"""
    reg = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"
    return validate(mac, reg)

