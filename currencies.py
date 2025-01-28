# pylint: disable=missing-docstring
"""
1.  Create a new constant dictionary called RATES at the top of currencies.py.
Keys will be 6-letter strings like "USDEUR", "GBPEUR", "CHFEUR"
The values will be their rate stored as a simple Python float number.
"""
RATES = {
    "USDEUR": 0.85,
    "GBPEUR": 1.13,
    "CHFEUR": 0.86,
    "EURGBP": 0.885
}

def convert(amount, target_currency):
    """Returns the converted amount in the given target_currency.

    amount is a tuple like (100, "USD")
    target_currency is a string
    """
    # 2a. Unpack tuple
    base_amount, base_currency = amount

    # 2b. Construct rate key
    f_x = base_currency + target_currency

    # 4. Get rate or None if doesnt exist
    rate = RATES.get(f_x)

    # 3. Return None if  rate unknown
    if rate is None:
        return None

    # return rounded converted value
    converted_value = round(base_amount * rate)
    return converted_value


print(convert((100, "USD"), "EUR"))  # Convert 100 USD to EUR
