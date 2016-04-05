from currency import Currency

class CurrencyConverter():
    def __init__(self, currency_dict):
#         self.code1 = code1
#         self.code2 = code2
#         self.amount = amount
        self.currency_dict = currency_dict
    # def convert(self):
    #     converted_amount = self.amount * (self.currency_dict.get(self.code2) / self.currency_dict.get(self.code1))
    #     #multiplies resulting variables of the two keys
    #     return converted_amount
        #returns amount and currency code.
    def convert2(self, current_currency, changed_currency):
        currency = current_currency.amount * (self.currency_dict.get(changed_currency) / self.currency_dict.get(current_currency.code))
        return Currency(changed_currency,currency)
    def get_rate(self, currency_code_source, currency_code_target):
        ex_rate = self.convert2(Currency(currency_code_source, 1), currency_code_target)
        return   ex_rate.amount
