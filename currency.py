############ Look for the nouns, verbs ###################

# nouns = variables, classes
# verbs = functions, methods

# first class
# an amount of currency
# magic methods
class Currency:
    '''A class that holds various currencies'''
# 1
    def __init__(self, amount, currency_code):
        self.amount = amount
        self.currency_code = currency_code

# 2 equal other currency_code with same amount and currency code
    def __eq__(self, other):
        return self.amount == other.amount and self.currency_code == other.currency_code

# 3 not equal to another with different amount or currency
    # __eq__ override and __add__ override
    def __ne__(self, other):
        return self.amount != other.amount or self.currency_code != other.currency_code

# 4.5 subtraction with same currency code
    def __sub__(self, other):
        if self.currency_code == other.currency_code:
            return Currency(self.amount - other.amount, self.currency_code)
        else:
            raise Exception ("You tried to add currencies of different countries!")
# 5 when __add__ or __subtract__ = raise Exception ("You tried to do a or s with
    # objects with different currency codes")
    def __add__(self, other):
        if self.currency_code == other.currency_code:
            return Currency(self.amount + other.amount, self.currency_code)
        else:
            raise Exception ("You tried to add currencies of different countries!")

# 6 = *(int) or *(float) and return object
    def __mul__(self, other):
        if self.amount
# 7 be able to recognize which currency is being used
    # ie ($1.20) the $ currency is being used

# to be able to print out the string(English) of the amount and the currency code
    def __str__(self):
        return str(self.amount) + '' + (self.currency_code)

user_input_currency = input("What currency would you like? ") 
user_input_amount = float(input("How much would you like to bring? "))
