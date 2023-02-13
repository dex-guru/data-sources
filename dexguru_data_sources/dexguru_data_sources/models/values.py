from pydantic import constr

address = constr(strict=True, strip_whitespace=True)
hex_color = constr(
    strict=True, min_length=4, max_length=7, strip_whitespace=True, to_lower=True, regex=r'^#[\da-f]+$'
)
rgba_color = constr(
    strict=True, min_length=13, max_length=24, strip_whitespace=True, to_lower=True,
    regex=r'^rgba\(\d{1,3},\s?\d{1,3},\s?\d{1,3},\s?\d(\.\d)?\)$'
)