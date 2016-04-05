
class Currency:
    def __init__(self, amount, currency_code):
        self.amount = amount
        self.currency_code = currency_code
​
    def __eq__(self, other):
        return self.amount == other.amount and self.currency_code == other.currency_code
​

    def __ne__(self, other):
        return self.amount != other.amount and self.currency_code != other.currency_code
​
    def __sub__(self, other):
        if self.currency_code == other.currency_code:
            return Currency(self.amount - other.amount, self.currency_code)
        else:
            raise Exception ("You tried to add currencies of different countries!")


    def __add__(self, other):
        if self.currency_code == other.currency_code:
            return Currency(self.amount + other.amount, self.currency_code)
        else:
            raise Exception ("You tried to add currencies of different countries!")
​
