
# because the CurrencyConverter inherits from the class Currency, must include
# it in ().
class CurrencyConverter(Currency):
# 1 initialized with {currency codes to conversion rates}
    # https://en.wikipedia.org/wiki/ISO_4217#Active_codes
    # http://www.xe.com/currencyconverter/#rates
# 2 must use the same currency code from Currency and return Currency = to one
    # that passed
# 3 take currency object(currency code) and requested (currency code) and return
    # new Currency object with right amount of currency code
# 4 must be able to be created with {of 3 or more $currency codes and conversion
    # rates} ie {'USD': 1.0, 'EUR': 0.74, 'JPY': 120.0}
# 5 must convert any $currency it knows from class Currency and convert it into
    # another $currency it knows from class Currency
# 6 if conversion error because currency not in class Currency, must raise
    # Exception ("Sorry, that currency is not available.")
