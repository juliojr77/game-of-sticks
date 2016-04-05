class Currency():
    def __init__(self, code, amount):
        self.code = code
        self.amount = amount
    def __str__(self):
        return str(self.amount) + ' ' + self.code
    def is_code(self, code):
        if self.code == code:
            return True
        else:
            return False
    def __eq__(self, code, amount):
        if self.code == code and self.amount == amount:
            return True
        else:
            return False
    def __add__(self, code, amount):
        if is_code(self, code):
            added = self.amount + amount
            return added
        else:
            raise DifferentCurrencyCodeError ("Currency Codes don't match")
    def subtract(self, code, amount):
        if is_code(self, code):
            subtracted = self.amount - amount
            return subtracted
        else:
            raise DifferentCurrencyCodeError ("Currency Codes don't match")
    def __mul__(self, code, amount, number):
        if is_code(self, code):
            multiplied = self.amount * float(number)
            return multiplied
        else:
            raise DifferentCurrencyCodeError ("Currency Codes don't match")
    def which_code(self, code):
        code_dict = {'$':'USD', '€':'EUR', '¥':'JPY'}
        if '$' in code_dict.keys():
            code = 'USD'
        elif '€' in code_dict.keys():
            code = 'EUR'
        elif '¥' in code_dict.keys():
            code = 'JPY'
        else:
            None
