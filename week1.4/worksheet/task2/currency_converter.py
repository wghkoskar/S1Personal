
"""
    Portfolio Task - Week 4

    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.

    Name: Oskar
"""

def currency_converter(amount, from_currency, to_currency):
    """
    A function that converts an amount from one currency to another
        Amount: A number representing the monetary value to be converted. It can be an integer or a
                floating-point number, and it must always be non-negative.

        from_currency: A string representing the currency code of the original currency. The supported
                       currency codes are:
                       GBP' (British Pound)
                      'CNY' (Chinese Yuan)
                      'PHP' (Philippine Peso)
                      'INR' (Indian Rupee)

        to_currency: A string representing the currency code to which the amount should be converted.
                     The possible values for this argument are the same as for from_currency
    """
    conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }
    from_selector = {}
    converter = 1
    for item in conversion_rate.keys():
        if from_currency == item:
            from_selector = conversion_rate.get(item)
    for item in from_selector.keys():
        if to_currency == item:
            converter = from_selector.get(item)

    # your code here

    if amount < 0:
        return 0.0
    else:
        return round(amount * converter, 2)

# Submit only this file currency_converter.py with the completed function.
# Remove any additional code you may have added during development and testing.
