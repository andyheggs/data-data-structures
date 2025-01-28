# pylint: disable=missing-docstring

# TODO: add some currency rates

"""
1.  Create a new constant dictionary called RATES at the top of currencies.py.
    Keys will be 6-letter strings like "USDEUR", "GBPEUR", "CHFEUR"
    The values will be their rate stored as a simple Python float number.
"""

RATES = {
        USDEUR: 0.85,
        GBPEUR: 1.13,
        CHFEUR: 0.86,
        EURGBP: 0.885
}

"""
2.  Implement the convert(amount, currency) function.
    The first parameter is a tuple of two elements: a float and a currency (e.g. (100, "USD")).
    The second parameter is a String, the currency you want to convert the amount into.

3.  You should round the results to the nearest whole number.

4.  When called with an unknown rate (e.g. "RMBEUR"), the convert function should return None.
"""

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """



 print(convert((100, "EUR"), "USD"))
