def parse_int(val_str, name="ID"):
    val = val_str.strip()
    if not val.isdigit():
        raise ValueError(f"{name} must be a positive number.")
    return int(val)

def validate_non_empty(val_str, name="Field"):
    cleaned = val_str.strip()
    if not cleaned:
        raise ValueError(f"{name} cannot be empty.")
    return cleaned
