import json
import re
from pathlib import Path

# Load area codes JSON
AREA_CODES_PATH = Path(__file__).parent / "area_codes.json"

with open(AREA_CODES_PATH, "r", encoding="utf-8") as f:
    AREA_CODE_MAP = json.load(f)


def normalize_phone_number(raw_input):
    if not raw_input or not isinstance(raw_input, str):
        return {"valid": False, "reason": "Invalid input"}

    raw = raw_input.strip()
    has_plus = raw.startswith("+")
    digits = re.sub(r"\D", "", raw)

    # Explicit international NANP
    if has_plus:
        if digits.startswith("1") and len(digits) == 11:
            return _build_nanp_result(digits)
        return {"valid": False, "reason": "Unsupported or invalid country code"}

    # NANP with country code
    if len(digits) == 11 and digits.startswith("1"):
        return _build_nanp_result(digits)

    # NANP without country code (assumed)
    if len(digits) == 10:
        return _build_nanp_result("1" + digits, assumed=True)

    return {"valid": False, "reason": "Invalid phone number length"}


def _build_nanp_result(digits, assumed=False):
    area_code = digits[1:4]
    location = AREA_CODE_MAP.get(area_code)

    result = {
        "valid": True,
        "e164": f"+{digits}",
        "plan": "NANP"
    }

    if assumed:
        result["warning"] = "Country code assumed (NANP)"

    if location:
        result["location"] = location
    else:
        result["location"] = "Unknown area code"

    return result
